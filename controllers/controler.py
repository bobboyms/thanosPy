from flask import json, jsonify, request
from functools import wraps
from configuracao import app
from flask_cors import CORS, cross_origin
from forms.TesteForm import TesteForm 
from architecture.construtor_de_formulario import obter_objeto_formulario

def requer_autenticacao(f):
    @wraps(f)
    def funcao_decorada(*args, **kwargs):
        print("antes")
        data = request.get_json()
        print(data)
        print("depois")

        return f(*args, **kwargs)
    return funcao_decorada

"""
def sleep(seconds=None):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Sleeping for {} seconds'.format(seconds))
            time.sleep(seconds if seconds else 1)
            return func(*args, **kwargs)
        return wrapper
    return real_decorator
"""

"""
Converte o Json
"""
def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            #obj = class_(**request.get_json())
            data = request.get_json()
            obj = class_(dicionario=data)
            return f(obj)
        return decorator
    return wrap

class Teste:
    def __init__(self,nome=None, dicionario=None):
        self.nome = nome

        if dicionario != None:
            self.__dict__.update(dicionario)

    def soma(self):
        pass

"""
"""
@app.route("/obter_formulario", methods=["GET"])
def obter_formulario():

    valor = obter_objeto_formulario()
    return json.dumps(valor)

"""
"""
@app.route("/enviar_formulario", methods=["POST"])
def submebter_formulario():

    dataForm = request.get_json()
    dicionario = dict()

    print("###################")

    #pega os valores recebidos da view
    for comp in dataForm["formulario"]:
        if comp["tipo"] == "text":
            if comp["type"] == "float":
                dicionario[comp["property"]] = float(comp["valor"])

    print(dicionario)

    ## aqui cria o objeto
    ## OBS: criar o objeto se ele não existir na memoria
    form = TesteForm(**dicionario)

    #executa o evento no servidor
    for comp in  dataForm["formulario"]:
       if comp["tipo"] == "evento":
           if comp["nome"] != "":
               func = getattr(form,comp["nome"])
               func()

    #atualiza a view
    for comp in dataForm["formulario"]:
       if comp["tipo"] == "text":
           comp["valor"] = form.__dict__[comp["property"]]

    print(dataForm)
    return json.dumps(dataForm)


"""
"""
@app.route("/", methods=["POST"])
@convert_input_to(Teste)
def hello(pessoa = None):
    
    print(type(pessoa))

    #dictJ = json.loads('{"nome": "thiago", "idade":20}')
    #thiago = Teste(dicionario=dictJ)

    for valor in pessoa.__dict__:
        
        if valor not in Teste.__dict__:
            print("o atributo %s nao existe na classe %s" % (valor, Teste.__name__))

        print("valor %s, tipo %s, instancia %s" % (valor, type(valor), isinstance(valor, str)))

    print(type(pessoa))
    print(isinstance(pessoa, Teste))

    return json.dumps(pessoa.__dict__)