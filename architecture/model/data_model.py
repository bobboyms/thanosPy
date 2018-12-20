class DataModel:
    
    def __init__(self, model_class = None):
        self.model_class = model_class

    def row_count(self):
        return len(self.model_class.query.all())

    def load_data(self, first, pageSize): #, sortField, sortOrder, filters
        
        print("FIRST %s" % first)
        print("PAGE SIZE %s" % pageSize)

        dados = self.model_class.query.offset(first).limit(pageSize + first)

        arr = []
        for car in dados:
            arr.append(car.as_dict()) 
        

        return arr