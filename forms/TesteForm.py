from models.Cliente import Cliente, Endereco
from models.Car import Car
from architecture.model.data_model import DataModel

class TesteForm:
    __soma = 10
    def __init__(self, valor_a =0, valor_b=0, resultado=0):
        self.valor_a = 0
        self.valor_b = valor_b
        self.resultado = resultado
        self.model_car = DataModel(Car)

        #self.dados = self.obter_dados()

        ende = Endereco("rua 2 de maio")
        self.cliente = Cliente("Thiago", "1234533", ende)
        
        #self.cliente = Cliente("Thiago", "1234533", Endereco("rua 2 de maio"))

    def obter_dados(self):
        #dados = Car.query.order_by(Car.id.desc()).paginate(page=1, per_page=10)

        dados = Car.query.offset(1).limit(40)

        arr = []
        for car in dados:
            arr.append(car.as_dict()) 

        return arr

    """
    Evento que soma alguma coisa
    """
    def eventoSoma(self):
        self.resultado = self.valor_a + self.valor_b
        print(self.cliente.nome)
        self.cliente.nome = "Taliba"
    
    def eventoSubtrai(self):
        self.__soma = self.__soma - 1
        self.resultado = self.__soma