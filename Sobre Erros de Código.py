'''
TIPOS DE ERROS COMUNS NO PYTHON:
SyntaxError (Erro de Sintaxe)
Ocorre quando o programador comete erro de digitação, esquece uma palavra-chave, caractere ou mesmo erra na indentação do código;

Erros por Exceções
Mesmo com a sintaxe correta, o programa pode sofrer um crash enquanto é executado por conta de algo não tratado durante o programa.
    *ZeroDivisionError - erro por divisão por zero
    *ValueError - erro de dado não esperado sendo digitado
    *IndexError - erro de índice inexistente sendo acessado
    *Lista completa de excessões: https://docs.python.org/3/library/exceptions.html

'''
# PODEMOS CONTORNAR OS ERROS NO CÓDIGO. VEJA:
i = 1
while True:
    try: # Solicita ao programa que tente rodar o comando abaixo.
        x = int(input('Por favor digite um número: '))
        break
    except ValueError: # Se o usuário não digitar um número, o comando abaixo é executado no lugar do erro convencional, permitindo que o looping estabelecido pelo While continue rodando.
        print("Oops! Número Inválido. Tente novamente...")
    finally: #acontece independente de erro ou acerto.
        print(f'Tentativa {i}')
        i += 1
print("número aceito.")  

# EXEMPLO 2:
def div():
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite um número: "))
        res = num1 / num2
        return res
    except ZeroDivisionError:
        print("Oops! Erro de divisão por zero...")
    except: #Aqui, todos os outros erros serão incluídos
        print("Algo de errado aconteceu...")
    
print(div())