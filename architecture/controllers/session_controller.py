class Session:

    __instance = None
    
    __forms_created = []

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Session.__instance == None:
            Session()
        return Session.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Session.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Session.__instance = self
    
    """
    Retorna um formulario se ele existir
    """
    def get_form_instance_session(self, id):
        
        for form in Session.__instance.__forms_created:
            if form["id"] == id:
                return form["class"]

        return None

    """
    
    """
    def create_form_instance_session(self,id, class_):
        Session.__instance.__forms_created.append({"id":id, "class":class_})


    