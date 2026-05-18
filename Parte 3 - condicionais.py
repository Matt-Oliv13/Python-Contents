'''
CONDICIONAIS
Usamos if (1º), else e elif (último) para estabelecer condicionais dentro de um algoritmo.
Ex:
'''
x = int(input("digite um número inteiro: "))
if (x % 2) == 0: #nº par sempre tem o resto da dívisão = 0, enquanto nº ímpar sempre tem o resto = 1
    print(f'Este número {x} é par!')
else:
    print(f'Este número {x} é ímpar!')

'''
OPERADORES LÓGICOS
Not (não) - negação de resultado booleano - Na prática: Ele inverte o valor lógico Ex: True vira False
And (e) - conjunção - somente é verdadeiro se, e somente se, ambas as entradas forem verdadeiras;
Or (ou) - disjunção - somente é verdadeiro se pelo menos uma das entradas for verdadeira;

Precedências:
Sempre que formos calcular com operadores lógicos:
1º Será visto dentro de parênteses;
2º Será feita operacão de potenciação e raízes;
3º Serão feitas operacoes aritmeticas de multiplicacao, divisao e modulo.
4º Operadores de adicao e subtracao
5º operadores relacionais (>, <, !=, ==);
6º operadores logicos not;
7º operadores logicos and;
8º operadores logicos or;
9º Por fim, são feitas as atribuicoes
'''
x = 10
y = 1
res1 = not x > y
print(res1) #Como o código realiza primeiro as operações relacionais, 10 > 1 -> True; not True = False

x = 10
y = 1
z = 5.5
res2 = (x > y) and (z==y)
print(res2) #Resolvendo: True 'and' False -> res = False

res3 = (x > y) or not z == y and y != (y + z) / x
print(res3) #Resolvendo: True or not False and True -> res = True

'''
CONDICIONAIS ANINHADAS
Basicamente é a inserção de condicionais dentro de outras condicionais
'''
#Escreva um algoritmo em que o usuario decide se vai comprar macãs, laranjas ou bananas.
#Após isso, deve-se digitar as quantidades que gostaria e o algoritmo deve calcular o preço e exibir.
#maçã = 2,30; laranjas = 3,60; e banana = 1,85 reais.

print("Bem vindo! Aqui você pode comprar:")
print("1. Maçãs")
print("2. Laranjas")
print("3. Bananas")
x = int(input("Digite o número da fruta que você deseja: "))
y = int(input("Agora digite a quantidade que você deseja: "))

if (x == 1):
    z = "Maçãs"
    res = float(y * 2.30)
    print(f'O valor do seu pedido de {z} custará R$ {res}')
elif (x == 2):
    z = "Laranjas"
    res = float(y * 3.60)
    print(f'O valor do seu pedido de {z} custará R$ {res}')
elif (x == 3):
    z = "Bananas"
    res = float(y * 1.85)
    print(f'O valor do seu pedido de {z} custará R$ {res}')
else: 
    print("Produto inexistente")

    

