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

            if obter_item_tratado(iten,"id") == "":
                id = str(uuid.uuid4())
            else:
                id = obter_item_tratado(iten,"id")

            if iten.tag == "inputText":
                component = {"tipo":"text", "id":id, "valor":obter_item_tratado(iten,"value"), "placeholder":obter_item_tratado(iten,"placeholder"), "label": obter_item_tratado(iten,"label")}
            elif iten.tag == "inputPassword":
                component = {"tipo":"password", "id":id, "valor":obter_item_tratado(iten,"value"), "placeholder":obter_item_tratado(iten,"placeholder"), "label": obter_item_tratado(iten,"label")}

            ##adiciona o componente no formulario
            formulario.append(component)


    return form

print(obter_objeto_formulario())