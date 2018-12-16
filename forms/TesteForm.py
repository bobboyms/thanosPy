class TesteForm:
    __soma = 10
    def __init__(self, valor_a, valor_b, resultado):
        self.valor_a = valor_a
        self.valor_b = valor_b
        self.resultado = resultado

    """
    Evento que soma alguma coisa
    """
    def eventoSoma(self):
        self.resultado = self.valor_a + self.valor_b
    
    def eventoSubtrai(self):
        self.__soma = self.__soma - 1
        self.resultado = self.__soma