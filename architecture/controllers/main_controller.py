from flask import json, jsonify, request
#from functools import wraps
from configuracao import app
#from flask_cors import CORS, cross_origin
from forms.TesteForm import TesteForm 
from architecture.construtor_de_formulario import obter_objeto_formulario
from architecture.utils.util import find_widget

"""
"""
@app.route("/main/obter_formulario", methods=["GET"])
def obter_formulario():

    valor = obter_objeto_formulario()
    return json.dumps(valor)

"""
"""

lista_formularios = []

@app.route("/main/enviar_formulario", methods=["POST"])
def submebter_formulario():

    dataForm = request.get_json()
    dicionario = dict()

    #pega os valores recebidos da view
    for comp in dataForm["formulario"]:
        if comp["tipo"] == "text":
            if comp["type"] == "float":
                if comp["valor"] == "":
                    dicionario[comp["property"]] = float(0.0)
                else:
                    dicionario[comp["property"]] = float(comp["valor"])

    ## aqui cria o objeto
    ## OBS: criar o objeto se ele não existir na memoria

    nome_formulario = "TesteForm"

    Class_ = find_widget(nome_formulario)
    form = Class_(**dicionario)

    lista.append(Class_)

    for cl in lista:
        print(cl)

    #executa o evento no servidor
    for comp in  dataForm["formulario"]:
       if comp["tipo"] == "evento":
           if comp["nome"] != "" or comp["nome"] != None:
               func = getattr(form,comp["nome"])
               func()

    #atualiza a view
    for comp in dataForm["formulario"]:
       if comp["tipo"] == "text":
            comp["valor"] = form.__dict__[comp["property"]]

    return json.dumps(dataForm)

