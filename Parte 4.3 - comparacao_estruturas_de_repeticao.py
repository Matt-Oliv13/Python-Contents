'''
No laço while, temos o valor inicial do iterador em uma varíável x e o valor final está na condição do while;
ex: x=*1* ; while x < *6*: ... -> Sendo o pulo/passo explícito na fórmula x=x+*2*

No laço for, temos o valor inicial do iterador no parenteses, antecedendo o final:
ex: for i in range(*1*, *6*, 2) -> Sendo o pulo/passo implícito no parenteses (2)
'''

#EXERCICIO: Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10. 
#3 Métodos:
#1) 2x while
tabuada = 1
while tabuada <= 10:
    print(f'tabuada do {tabuada}:')
    i = 1
    while i <= 10:
        print(f'{tabuada}x{i}={tabuada*i}')
        i += 1 # o mesmo que dizer i = i+1
    tabuada += 1 # o mesmo que dizer tabuada = tabuada + 1; Quando todos os i forem usados (i>10), a tabuada aumenta de valor e o loop recomeça.

#2) 2x for
for tabuada in range(1, 11, 1):
    print(f'TABUADA do {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * i}')

#3) While + for
tabuada = 1
while tabuada <= 10:
    print(f'TABUADA DO {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada}x{i} = {tabuada}*{i}')
    tabuada += 1
