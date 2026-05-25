'''
Escreva uma função que calcule o fatorial de um nº recebido como parâmetro e retorne o resultado. Faça uma validação dos dados por meio de uma outra função, permitindo que somente nº positivos sejam aceitos. Crie o help da sua função.
'''
#Fatorial de X = X . X-1 . X-2 . X-3 . X-4 

#MEU DESENVOLVIMENTO:
def validacao(x):
    global valor
    while x < 0:
        try: 
            x = int(input("Digite um número inteiro positivo: "))
            if x < 0:
                print("Este número não é válido.")
            else: 
                valor = x
                print(x)
        except: 
            print(f"Caracteres inválidos.")


def calcular_fatorial(x):
    """
    Função que calcula a fatorial de um número inteiro positivo.
    """
    if x < 0:
        return "Fatorial não existe para números negativos"
    
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i 
        # O mesmo que escrever resultado = resultado * i
        # 1*1, 1*2, 2*3, 6*4, 24*5, ... resultado*x+1
    return (f"O fatorial de {x} é {resultado}!")

valor= -1
primeiro = validacao(valor)
res = calcular_fatorial(valor)
print(res)
help(calcular_fatorial)

#-------------------------------------------------------------
# MÉTODO DO MATERIAL:
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x<min) or (x>max)):
        x = int(input(pergunta))
    return x

def fatorial (num):
    """
    Função que calcula a fatorial de um número inteiro positivo.
    :param: num
    :return: 
    """
    fat = 1
    if num == 0:
        return fat # 0! = 1
    elif num > 0:
        for i in range(1, num + 1):
            fat *= i 
            # O mesmo que escrever fat = fat * i
            # 1*1, 1*2, 2*3, 6*4, 24*5, ... fat*x+1
        return (f"O fatorial de {num} é {fat}!")
    elif num < 0:
        return "Fatorial não existe para números negativos"
    else:
        return "Caracteres inválidos. Tente novamente."

x = valida_int('Digite um valor para calcular o fatorial: ', 0, 99999)
print(f'{x}! = {fatorial(x)}')
help(fatorial)

#---------------------------------------------------------------------------