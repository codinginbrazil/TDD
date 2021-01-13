## To Do: :dart:
`test:`
* $5 + 10 CHF = $10 se a taxa é 2:1
* Arredondamento de dinheiro
* hashCode()
* Igualdade de null
* Igualdade de objeto


---

### 0.4 Privacy
* Tornar “amount” privada / métodos de acesso 
    * [property](https://docs.python.org/3/library/functions.html#property)
    
refactor: test_multiplication

*test_dollar()*

### 0.3 Equality for all
`test:` equals() :heavy_check_mark:
* percebemos que nosso padrão de projeto (Value Object) sugeria uma operação
* testamos para aquela operação
* implementamos de uma forma simples
* não refatoramos imediatamente, mas, em vez disso, testamos mais
* refatoramos para capturar os dois casos de uma só vez


### 0.2 Degenerate Objects
`test:` *Efeitos colaterais em Dollar* :heavy_check_mark:

duas das três estratégias que conheço para chegar rapidamente ao verde:
* engane-o: retorne uma constante e 
    gradualmente substitua constantes por variáveis até ter o código real.
* use implementação óbvia: codifique a implementação real.

:heavy_plus_sign: logging

:heavy_minus_sign: requirements

### 0.1 Dependency and Duplication
`test:` *$5 * 2 = $10* :heavy_check_mark:

refactor

referência:
* :heavy_minus_sign: Wazlawick, Raul Sidnei. Introdução a Algoritmos e Programação com Python: Uma abordagem dirigida por testes. Elsevier, 2017 

---

### 0.0.1
assertion: verificar se o código não está fazendo nada obviamente incorreto.
* a palavra-chave assert;
* uma condição (ou seja, uma expressão avaliada como True ou False);
* uma vírgula;
* uma string a ser exibida quando a condição for False.

ritmo do desenvolvimento guiado por testes
1. Adicionar um teste rapidamente.
2. Rodar todos os testes e ver o mais novo falhando.
3. Fazer uma pequena mudança.
4. Rodar todos os testes e ver todos funcionando.
5. Refatorar para remover duplicações.

referência
* Beck, Kent TDD Desenvolvimento Guiado por Testes Livro por Kent Beck. 2010
* Sweigart, Al. Automatize Tarefas Maçantes com Python, p. 266 
* Matthes, Eric. Python Crash Course: A Hands-On, Project-Based Introduction to Programming, p. 215
* Wazlawick, Raul Sidnei. Introdução a Algoritmos e Programação com Python: Uma abordagem dirigida por testes. Elsevier, 2017 
