'''
Laço 'while' (enquanto)
Para resolver problemas em que precisamos repetir determinadas linhas de código enquanto determinada condição for verdadeira, usamos o laço while. Quando a condição não for mais verdadeira, o loop se encerra.
'''
x = 0
while x <= 5: # Ou seja, enquanto x < 5, repita as linhas a seguir:
    print(x)
    x = x + 1
print("Encerrada a contagem") # Quando x = 6, o loop encerra e essa linha é lida.

# Variável de controle (ou Iterador) é a variável que realiza a contagem do número de vezes que o laço está sendo executado. Neste exemplo, x é o iterador. Podem ser de dois tipos:
#   * Contadores - acrescentam valores constantes em uma variável
#   * Acumuladores - acumulam totais, comoum somatório

#EXERCÍCIO PRÁTICO: Escrever um algoritmo que imprima na tela somente valores dentro de um intervalo especificado pelo usuário e que sejam números pares.

x = int(input("Digite um número de 0 à 10: "))
y = int(input("Digite um número de 10 à 30: "))
print(x)
print(y)
if x <= 10 and y >= 10 and y <= 30:
    while x <= y:
        if (x % 2 == 0): # Aqui verificamos se o número a ser contado é par. Se não for, não será exibido, mas modificará a variável 'x'.
            print(x)
        x = x + 1
else:
    print("Digite um número válido")
print("Contagem terminada para o intervalo escolhido")

#EXERCÍCIO PRÁTICO 2: Escreva um algoritmo que calcule a sua média de notas em determinada disciplina. Assuma que a média final é dada pela média aritmética de cinco notas digitadas.

soma = 0
cont = 1
while (cont<=5):
    x = float(input(f'Digite a {cont}ª nota: '))
    soma = soma + x
    cont = cont + 1
media = soma/5
print(f'Média final: {media}')

# Operadores Especiais de Atribuição (Veja a imagem correspondente no repositório)

#EXERCÍCIO PRÁTICO 3: Crie um algoritmo que receba um valor do tipo inteiro via teclado. No entanto, o programa só deve aceitar valores inteiros e positivos. Qualquer valor negativo, ou igual a zero, deve ser rejeitado e um novo valor deve ser solicitado.

x = int(input("Digite um valor maior que 0: "))
while x<=0:
    x=int(input("Digite um valor maior que 0: "))
print(f'Você digitou {x}. Encerrando o programa...')

# A instrução break serve para encerrar um laço de repetição abruptamente, independente do estado da variável de controle do laço. EXEMPLO:
print('Digite uma mensagem que irei repetir para você!')
print("Para encerrar, escreva 'sair'.")
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print("Encerrando programa...")

# A instrução continue serve para retornar o laço ao início a qualquer momento, independentemente do estado da variável de controle da condicional do laço.
# Atenção ao exemplo!
while True:
    nome = input('Digite seu usuário: ')
    if nome != 'desenvolvedor':
        continue # volta para o início do laço
    senha = input('Digite sua senha: ')
    if senha == 'senha123': 
        break # encerra o laço
    # Se a senha for diferente, reinicia todo o laço
print('Acesso concedido.')

#=======================================

# Valores Truthy e Falsey em condições envolvendo dados não booleanos:
# O python reconhece o número '0' (int ou float) e strings vazias como False, e para não confundir com o false (booleano), é chamado de Falsey.
# Do mesmo modo, qualquer outro valor não booleano é chamado de Truthy.
nome = '' #Falsey
while not nome: # Equivale a 'not Falsey' (Truthy/True)
    # encerra o laço quando nome não for vazio
    nome = input('Digite seu nome: ')

valor = int(input('Digite um número qualquer: '))
if valor: #Equivale a 'if valor != 0' -> Se o usuário digita 0, passa a ser falso
    print('Você digitou um valor diferente de zero.')
else:
    print('Você digitou zero.')

#====================================



