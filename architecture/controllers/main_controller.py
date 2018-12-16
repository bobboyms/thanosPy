from flask import json, jsonify, request
#from functools import wraps
from configuracao import app
#from flask_cors import CORS, cross_origin
from forms.TesteForm import TesteForm 
from architecture.construtor_de_formulario import obter_objeto_formulario
from architecture.utils.util import find_widget
from architecture.controllers.session_controller import Session


def get_dict_form(dataForm):
    
    dicionario = dict()

    #pega os valores recebidos da view
    for comp in dataForm["formulario"]["componentes"]:
        if comp["tipo"] == "text":
            if comp["type"] == "float":
                if comp["valor"] == "":
                    dicionario[comp["property"]] = float(0.0)
                else:
                    dicionario[comp["property"]] = float(comp["valor"])

    return dicionario

"""
"""
def get_instance_form(dataForm):    
    
    session = Session.getInstance()

    nome_formulario = dataForm["formulario"]["name_form"]
    id_formulario = dataForm["formulario"]["id_formulario"]

    instance = session.get_form_instance_session(id_formulario)

    if instance != None:
        print("USOU UM FORM")
        dicionario = get_dict_form(dataForm)
        instance.__dict__.update(dicionario)

        return instance

    print("CRIOU UM FORM")
    dicionario = get_dict_form(dataForm)

    ## aqui cria o objeto
    ## OBS: criar o objeto se ele não existir na memoria
    Class_ = find_widget(nome_formulario)
    form = Class_(**dicionario)

    session.create_form_instance_session(id_formulario,form)

    return form

"""
"""
@app.route("/main/obter_formulario", methods=["GET"])
def obter_formulario():

    dataForm = obter_objeto_formulario()

    print("###############")
    print(dataForm)

    form = get_instance_form(dataForm)

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
    for comp in dataForm["formulario"]["componentes"]:
       if comp["tipo"] == "text":
            comp["valor"] = form.__dict__[comp["property"]]

    return json.dumps(dataForm)

