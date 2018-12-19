import uuid
import xml.etree.ElementTree as ET

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
def obter_id_unico(iten = None):
    if iten == None or obter_item_tratado(iten,"id") == "":
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

    componentes = []
    
    formulario = {
        "name_form":"TesteForm",
        "id_formulario":obter_id_unico(),
        "evento_atual":"",
        "componentes":componentes,
    }
    
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
            elif iten.tag == "dataTable":
                component = {
                              "tipo":"dataTable", 
                              "id":obter_id_unico(iten),
                              "property":obter_item_tratado(iten,"property"),
                              "items": [], 
                              "datasource" : [],
                              "loading": False,
                              "first": 0,
                              "rows": 10,
                              "totalRecords": 0,
                            }       
          #componente.datasource = data;
          #componente["totalRecords"] = data.length,
          #componente["items"] = componente.datasource.slice(0, componente.rows),
          #componente["loading"] = false


            if component != None:
                ##adiciona o componente no formulario
                componentes.append(component)

    formulario["evento_atual"] = ""

    print(form)

    return form

print(obter_objeto_formulario())