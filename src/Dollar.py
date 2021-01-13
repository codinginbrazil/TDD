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
        logging.debug('self.amount: ' + str(self._amount))
     
     
    @property
    def amount(self):
        return self._amount 
    
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount
        
  
    @amount.deleter
    def amount(self):
        del self._amount
        
        
    def equals(self, object) -> bool:
        try:
            return self.amount == object.amount
        except:
            logging.WARNING('Error: Object is not a Dollar')


    def dollar(self, amount) -> None:
        self.amount = amount
        
        logging.debug('dollar')
        logging.debug('amount: ' + str(amount))
        logging.debug('self.amount: ' + str(self.amount))


    def times(self, multiplier):        
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
    
    ''' Níveis de logging
        DEBUG
            Função de logging: logging.debug()
            Descrição: Usado para pequenos detalhes. 
                Geralmente, você estará interessado nessas mensagens 
                somente quando estiver diagnosticando problemas.
        
        INFO
            Função de logging: logging.info()
            Descrição: Usado para registrar informações sobre eventos 
                em geral em seu programa ou para confirmar 
                se tudo está funcionando nesse ponto do programa.
            
        WARNING
            Função de logging: logging.warning()
            Descrição: Usado para indicar um problema em potencial 
                que não impede o programa de funcionar, 
                porém poderá fazer isso no futuro.
            
        ERROR
            Função de logging: logging.error()
            Descrição: Usado para registrar um erro que fez o programa falhar em fazer algo.
            
        CRITICAL
            Função de logging: logging.critical()
            Descrição: É o nível mais alto. 
                Usado para indicar um erro fatal que fez ou 
                está prestes a fazer o programa parar totalmente de executar.
        
        Referência: 
            Sweigart, Al. Automatize Tarefas Maçantes Com Python - 
                Programação Prática Para Verdadeiros Iniciantes. p. 274. 2015
    '''