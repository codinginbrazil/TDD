market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
            switchLights(market_2nd)
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
        

if __name__ == "__main__":
    try: 
        switchLights(market_2nd)
    except: 
        print('Error')


''' simulação de semáforo: requisitos 
    
    Usando uma asserção em uma simulação de semáforo
    
    Suponha que você esteja criando um programa de simulação de semáforo. 
    
    A estrutura de dados que representa os semáforos 
    em uma intersecção é um dicionário com chaves 'ns' e 'ew' 
    para os semáforos voltados na direção norte-sul e leste-oeste, respectivamente.
     
    Os valores dessas chaves serão as strings 'green', 'yellow' ou 'red'. 
    
    Essas duas variáveis representam as intersecções entre a Market Street 
    e a 2nd Street e entre a Mission Street e a 16th Street. 

    Para iniciar o projeto, queremos criar uma função switchLights() 
    que aceitará um dicionário referente a uma intersecção como argumento
    e mudará as luzes do semáforo.
    
    
    Para desabilitar as instruções assert em seus programas Python 
    para ter uma pequena melhoria no desempenho. 
    
    Ao executar o Python a partir do terminal, 
    inclua a opção -O após python ou 
    python3 e antes do nome do arquivo .py. 
    
    Isso fará uma versão otimizada de seu programa ser executada,
    em que as verificações de asserção serão ignoradas.

'''