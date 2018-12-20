import types
from flask import json, jsonify, request
#from functools import wraps
from configuracao import app
#from flask_cors import CORS, cross_origin
from forms.TesteForm import TesteForm 
from architecture.construtor_de_formulario import obter_objeto_formulario
from architecture.utils.util import find_widget
from architecture.controllers.session_controller import Session

from models.Car import Car

"""
Obtem o valor do atributo da classe no formato convertido
"""
def get_value_casting(comp, attr):

    if comp["type"] == "float":
        
        if type(attr) == str and len(attr) == 0:
            return 0

        if type(attr) == float and attr == 0:
            return 0

        if type(attr) == int and attr == 0:
            return 0

        return float(attr)
    else:
        return attr

"""
Obtem valor de uma propriedade dentro da clace
"""
def get_value_attr(attr, comp):

    print("ATTR %s" % attr)

    if "." in comp["property"]:
            
        props = comp["property"].split(".")
            
        for prop in props:
            attr = getattr(attr, prop)
        
        return attr

    else:
        attr = getattr(attr, comp["property"])
        return attr

"""
Seta valores recebidos da view e adicona na classe
"""
def set_value_attr(attr, comp, inicial = False):
    
    instance = None
    count = 0
    if "." in comp["property"]:
        
        props = comp["property"].split(".")
        
        for prop in props:
            print("===================")
            print(prop)
            attr = getattr(attr, prop)
            count += 1
            if len(props) > count:
               instance = attr
        
        nome_prop = props[len(props) -1]
        instance.__dict__[nome_prop] = get_value_casting(comp, comp["valor"])
            
    else:
        attr.__dict__[comp["property"]] = get_value_casting(comp, comp["valor"])

"""
Pega os valores da classe Form e adiciona no dicionario para enviar para VIEW
"""
def update_view(form, dataForm):
    #atualiza a view
    for comp in dataForm["formulario"]["componentes"]:
        if comp["tipo"] == "text":

            attr = get_value_attr(form, comp)

            if type(attr) == types.MethodType:
                comp["valor"] = attr()
            else:
                comp["valor"] = attr

            
        elif comp["tipo"] == "dataTable":

            attr = get_value_attr(form, comp)

            if comp["use_data_model"] == True:
                
                toal_registros = attr.row_count()
                itens = attr.load_data(first=comp["first"], pageSize=comp["rows"])

                comp["items"] = itens
                comp["totalRecords"] = toal_registros

            else:
                if type(attr) == types.MethodType:
                    comp["items"] = attr()
                    comp["datasource"] = attr()
                    comp["totalRecords"] = len(attr())
                else:
                    comp["items"] = attr
                    comp["datasource"] = attr
                    comp["totalRecords"] = len(attr)
                

"""
"""
def get_instance_form(dataForm):    
    
    session = Session.getInstance()

    nome_formulario = dataForm["formulario"]["name_form"]
    id_formulario = dataForm["formulario"]["id_formulario"]

    instance = session.get_form_instance_session(id_formulario)

    #########################################
    #
    # se existir uma instancia
    #
    if instance != None:
        #dicionario = get_dict_form(dataForm)
        #instance.__dict__.update(dicionario)
        for comp in dataForm["formulario"]["componentes"]:
            if comp["tipo"] != "button" and comp["tipo"] != "dataTable":
                set_value_attr(instance,comp)
        
        return instance

    ########################################
    #
    # se nao existir uma instancia

    ## aqui cria o objeto
    ## OBS: criar o objeto se ele não existir na memoria
    Class_ = find_widget(nome_formulario)
    instance = Class_()

    print(instance)

    # for comp in dataForm["formulario"]["componentes"]:
    #         if comp["tipo"] != "button":
    #             set_value_attr(instance,comp,inicial=True)

    session.create_form_instance_session(id_formulario,instance)

    return instance

"""
"""
@app.route("/main/obter_formulario", methods=["GET"])
def obter_formulario():

    dataForm = obter_objeto_formulario()
    form = get_instance_form(dataForm)

    if form == None:
        raise Exception("Nenhum formulario encontrado")

    #atualiza a view
    update_view(form,dataForm)

    print(dataForm)

    return json.dumps(dataForm)

"""
"""
@app.route("/main/enviar_formulario", methods=["POST"])
def submebter_formulario():

    dataForm = request.get_json()
    form = get_instance_form(dataForm)

    #executa o evento no servidor
    nome_evento = dataForm["formulario"]["evento_atual"]
    func = getattr(form,nome_evento)
    func()

    #atualiza a view
    update_view(form,dataForm)


    return json.dumps(dataForm)


@app.route("/main/obter_carros", methods=["GET"])
def obter_carros():
    dados = Car.query.all()
    arr = []
    for car in dados:
        arr.append(car.as_dict()) 
    
    #print(contactsArr)
    #return '{"data":[{"vin":"a1653d4d","brand":"Volkswagen","year":1998,"color":"White"}]}'
    return json.dumps({"data":arr})