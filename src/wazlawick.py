import logging


logging.basicConfig(level=logging.DEBUG, 
                    format=' %(asctime)s - %(levelname)s - %(message)s')

# logging.disable()


def division(numerator, divider):
    logging.debug('Start of division '+ str(numerator) + '/' + str(divider))
    try:
        logging.debug('Result is ' + str(numerator / divider))
        return numerator / divider
    except ZeroDivisionError:
        logging.error('Zero Division Error')
        return None


if __name__ == "__main__":
    logging.debug('Start of program')
    
    division(12, 10)
    division(3, 1)
    division(14, 0)
    
    logging.debug('End of program')
    
    
''' Níveis de logging
    DEBUG
        Função de logging: logging.debug()
        Descrição: Usado para pequenos detalhes. 
            Geralmente, você estará interessado nessas mensagens somente quando estiver diagnosticando problemas.
    
    INFO
        Função de logging: logging.info()
        Descrição: Usado para registrar informações sobre eventos em geral em seu programa 
            ou para confirmar se tudo está funcionando nesse ponto do programa.
        
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