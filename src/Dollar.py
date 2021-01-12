class Dollar(object):
    
    def __init__(self):
        self.amount = 0


    def dollar(self, amount) -> None:
        self.amount = amount


    def times(self, multiplier) -> None :
        self.amount *= multiplier
    

    ''' Requisitos
        Precisamos ser capazes de somar valores em duas moedas diferentes e de
            converter o resultado, dado um conjunto de taxas de câmbio.
        Precisamos ser capazes de multiplicar um valor (preço por ação) por um
            número (número de ações) e de receber uma quantia.
    '''