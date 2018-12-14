import uuid
import xml.etree.ElementTree as ET
import flask from session

"""

"""
def obter_item_tratado(iten, att):
    if iten.get(att) == None or len(iten.get(att)) == 0:
        return ""
    else:
        return iten.get(att)

"""
Função que cria um identificador unico
"""
def obter_id_unico(iten):
    if obter_item_tratado(iten,"id") == "":
        return str(uuid.uuid4())
    else:
        return obter_item_tratado(iten,"id")

"""
"""
def obter_option_do_iten(iten):
    opts = []
    for options in iten:
        for option in options:
            valor = {"valor":obter_item_tratado(option,"valor"), "id":obter_id_unico(option)}
            opts.append(valor)

    return opts

"""
FUNÇÃO: Le um arquivo XML que representa um formulario
Retorna um objeto do tipo dict que contem uma lista de componentes
"""
def obter_objeto_formulario():
    
    tree = ET.parse('formularios/itens.xml')  
    root = tree.getroot()

    formulario = []
    form = {"formulario":formulario}

    for elementos in root:
        for iten in elementos:
            component = None
            if iten.tag == "inputText":
                component = {
                                "tipo":"text", "id":obter_id_unico(iten), 
                                "valor":obter_item_tratado(iten,"value"), 
                                "placeholder":obter_item_tratado(iten,"placeholder"), 
                                "label": obter_item_tratado(iten,"label"), 
                                "property":obter_item_tratado(iten,"property"),
                                "type":obter_item_tratado(iten,"type")
                            }
            elif iten.tag == "inputPassword":
                component = {
                                "tipo":"password", 
                                "id":obter_id_unico(iten), 
                                "valor":obter_item_tratado(iten,"value"), 
                                "placeholder":obter_item_tratado(iten,"placeholder"), 
                                "label": obter_item_tratado(iten,"label")
                            }
            elif iten.tag == "select":
                opts = obter_option_do_iten(iten)
                component = {
                                "tipo":"select",
                                "id":obter_id_unico(iten), 
                                "label":obter_item_tratado(iten,"label"), 
                                "index":"", 
                                "idDetail":"", 
                                "valor":"", 
                                "options":opts
                            }
            elif iten.tag == "radio": 
                opts = obter_option_do_iten(iten)
                component = {
                                "tipo":"radio",
                                "id":obter_id_unico(iten), 
                                "label":obter_item_tratado(iten,"label"), 
                                "index":"", 
                                "idDetail":"", 
                                "valor":"", 
                                "options":opts
                            }
            elif iten.tag == "checkbox":    
                opts = obter_option_do_iten(iten)
                component = {
                                "tipo":"checkbox",
                                "id":obter_id_unico(iten), 
                                "label":obter_item_tratado(iten,"label"), 
                                "valores":[], 
                                "options":opts
                            }    
            elif iten.tag == "button":
                component = {
                                "tipo":"button", 
                                "id":obter_id_unico(iten), 
                                "evento":obter_item_tratado(iten,"event"), 
                                "label": obter_item_tratado(iten,"label")
                            }

            if component != None:
                ##adiciona o componente no formulario
                formulario.append(component)

    formulario.append({"tipo":"evento", "nome":""})
    return form

print(obter_objeto_formulario())