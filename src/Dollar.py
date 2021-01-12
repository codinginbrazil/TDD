import logging


logging.basicConfig(filename=('log/dollar.txt'),
                    level=logging.DEBUG, 
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable()
logging.debug('Start of program')


class Dollar(object):
    
    def __init__(self, amount):
        self.amount = amount
        
        logging.debug('__init__')
        logging.debug('amount: ' + str(amount))
        logging.debug('self.amount: ' + str(self.amount))


    def dollar(self, amount) -> None:
        self.amount = amount
        
        logging.debug('dollar')
        logging.debug('amount: ' + str(amount))
        logging.debug('self.amount: ' + str(self.amount))


    def times(self, multiplier) -> None :        
        logging.debug('times')
        logging.debug('multipliear: ' + str(multiplier))
        logging.debug('self.amount: ' + str(self.amount))
        
        return (self.amount * multiplier)
        
        logging.debug('self.amount: ' + str(self.amount))
        

    ''' Requisitos
        Precisamos ser capazes de somar valores em duas moedas diferentes e de
            converter o resultado, dado um conjunto de taxas de câmbio.
        Precisamos ser capazes de multiplicar um valor (preço por ação) por um
            número (número de ações) e de receber uma quantia.
    '''