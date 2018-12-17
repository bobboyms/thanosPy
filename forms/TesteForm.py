from models.Cliente import Cliente, Endereco

class TesteForm:
    __soma = 10
    def __init__(self, valor_a =0, valor_b=0, resultado=0):
        self.valor_a = 0
        self.valor_b = valor_b
        self.resultado = resultado

        ende = Endereco("rua 2 de maio")

        self.cliente = Cliente("Thiago", "1234533", ende)
        
        #self.cliente = Cliente("Thiago", "1234533", Endereco("rua 2 de maio"))

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