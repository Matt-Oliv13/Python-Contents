#Exercício (1) Realize a sequência de print com for e while:
# a) Inteiros de 3 a 12, com 12 incluso;
# b) Inteiros de 0 a 9, excluindo 9, com passo de 2.

# RESOLUÇÃO (a):
for i in range (3, 13):
    print(i)

x = 3
while x < 13:
    print(x)
    x += 1

# Resolução (b):
for i in range (0, 9, 2):
    print(i)

x=0
while x < 9:
    print(x)
    x+=1

#------------------------------

# Exercício (2) Escreva um algoritmo que mostra, na tela, quatro produtos a serem comprados em uma lanchonete, depois permita selecionar o produto e dê o valor total do pedido: 
# Coxinha - R$5,00
# Pastel - R$ 7,00
# Café - R$ 4,00
# Suco - R$ 6,00

print("Os produtos que temos disponíveis são:")
print("1 - Coxinha R$ 5,00")
print("2 - Pastel R$ 7,00")
print("3 - Café R$ 4,00")
print("4 - Suco R$ 6,00")

total = 0 
while True:
    item = int(input("Digite o nº do item desejado: "))
    if item == 1:
        valor = 5.00
    elif item == 2:
        valor = 7.00
    elif item == 3:
        valor = 4.00
    elif item == 4:
        valor = 6.00
    else:
        print("comando inválido")
        continue    
    quantidade = int(input("Digite a quantidade desejada: "))
    total = total + (valor * quantidade)
    desejo = input("Deseja acrescentar algo no pedido (sim ou não)? ")
    if desejo == "sim":
        continue
    elif desejo == "não":
        break
    else:
        print("comando inválido")
print(f"Pedido realizado no valor de R$ {total}!")

#------------------------------------------

# Exercício (3) Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor. Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 1.

valor = int(input("Digite um valor em R$: "))

while True:
    if valor >= 100:
        cedulas100 = valor // 100 # Aqui descontaremos o valor em notas de 100 para simplificar, caso o valor seja mais alto.
        valor = valor - cedulas100 * 100 
        print(f'Cédulas de 100: {cedulas100}')
        continue # Ao invés de "continue" poderíamos usar "If not valor:" e em uma linha identada abaixo "break" para cada valor de cédula (100, 50, ...)

    elif valor < 100 and valor >= 50:
        cedulas50 = valor // 50 # Aqui descontaremos o valor em notas de 50 para simplificar, caso o valor seja mais alto.
        valor = valor - cedulas50 * 50 
        print(f'Cédulas de 50: {cedulas50}')
        continue

    elif valor < 50 and valor >= 20:
        cedulas20 = valor // 20 # Aqui descontaremos o valor em notas de 20 para simplificar, caso o valor seja mais alto.
        valor = valor - cedulas20 * 20 
        print(f'Cédulas de 20: {cedulas20}')
        continue

    elif valor < 20 and valor >= 10:
        cedulas10 = valor // 10 # Aqui descontaremos o valor em notas de 10 para simplificar, caso o valor seja mais alto.
        valor = valor - cedulas10 * 10 
        print(f'Cédulas de 10: {cedulas10}')
        continue

    elif valor < 10 and valor >= 5:
        cedulas5 = valor // 5 # Aqui descontaremos o valor em notas de 5 para simplificar, caso o valor seja mais alto.
        valor = valor - cedulas5 * 5 
        print(f'Cédulas de 5: {cedulas5}')
        continue

    elif valor < 5 and valor >= 2:
        cedulas2 = valor // 2 # Aqui descontaremos o valor em notas de 2 para simplificar, caso o valor seja mais alto.
        valor = valor - cedulas2 * 2 
        print(f'Cédulas de 2: {cedulas2}')
        continue

    elif valor < 2 and valor >= 1:
        cedula1 = valor # Aqui pode sobrar somente uma cédula.
        valor = valor - cedula1 * 1 
        print(f'Cédula de 1: {cedula1}')
        break

print("Contagem encerrada!")

#--------------------------------------

