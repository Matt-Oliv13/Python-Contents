'''
1) Escreva o somatório dos 5 primeiros números inteiros positivos
'''
print(1+2+3+4+5)
'''
------------------------------------------------------------------
2) A média entre 19, 23 e 31
'''
resultado = int((19+23+31)/3)
print(f'Seu resultado é {resultado}')
'''
------------------------------------------------------------------
3) o número de vezes que 73 cabe em 403
'''
lista = []
n = 0
while n + 73 <= 403:
    n = n + 73
    lista.append(n)
print(len(lista))

#Esse problema poderia ter sido resolvido de forma mais simples:
print(403//73)
'''
-----------------------------------------------------------------
4) A sobra quando 403 é dividido por 73
'''
print(403%73)
'''
-----------------------------------------------------------------
5)
Escreva 2 elevado a 10
O valor absoluto da diferença entre 54 e 57
O menor valor entre 34, 29 e 31
'''
print(2**10)
print(abs(54-57))
print(min(29, 31, 34))
'''
------------------------------------------------------------------
6) Atribuição de valores
'''
a = 3
b = 4
c = a*a + b*b
print(c)
'''
------------------------------------------------------------------
7) Strings
'''
s1='ant'
s2='bat'
s3='cod'
res = s1+s2+s3
print(res)
res = s1+''+s2+''+s3
print(res)
res = s1*10
print(res)
res = s1+s2*2+s3*3
print(res)
'''
------------------------------------------------------------------
8) Desafio 1 - Colocar um input para valor de um produto e seu desconto, depois exiba
'''
valor=float(input("Digite o preço do produto: "))
porcentagem = float(input("Digite o valor do desconto (0-100%): "))
valor_desconto = (valor*porcentagem)/100
print(f"O valor do seu desconto foi {valor_desconto} e o valor final do produto é {valor-valor_desconto}")

'''
------------------------------------------------------------------
9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como
a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00
por dia e R$0,15 por km rodado
'''
km = float(input("Quantos km foram rodados? "))
dias = int(input("Por quantos dias o carro foi alugado? "))
preco = dias*60 + km*0.15
print(f'O valor à pagar é R${preco}')
'''
------------------------------------------------------------------
10)crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável, agora contendo metade
da string digitada. Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string.
'''
frase = input("Digite uma frase: ")
tam = len(frase) #Para termos a quantidade de caracteres da frase
frase2 = frase[0:int(tam/2)] # Aqui frase2 = quantidade de caracteres de 'frase' até 'tam/2'. 
#Colocamos int pois não queremos decimais --> Isso geraria um erro se a frase tivesse 'tam' ímpar.
print(frase2)
print(frase2[-2:]) # Como só queremos os último 2 elementos, podemos colocar a referência negativa.
#Assim, serão considerados os últimos dois caracteres da variavel.
