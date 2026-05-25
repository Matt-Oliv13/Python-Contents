'''
MANIPULAÇÃO DE ARQUIVOS
Aqui veremos como manipular arquivos com um exercício prático, com um número variado de funções!
'''

#Exercicio (4) Escreva um algoritmo que permita cadastrar jogos informando o nome e a qual videogame pertence. Para isso, crie um menu de opções contendo: cadastrar novo item, listar tudo que foi cadastrado e sair. Para resolver esse exercício, crie uma função para cada item do menu. Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter todos os dados cadastrados.

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x<min) or (x>max)):
        x = int(input(pergunta))
    return x

def existe_arquivo(nomeArquivo):
    try: 
        a = open(nomeArquivo, 'rt') #open ( , read) - modo de leitura
        a.close() #Sempre feche o arquivo para não deixá-lo aberto, mesmo depois de fechar o programa.
    except FileNotFoundError:
        return False
    else: return True

def criarArquivo(nomeArquivo):
    try: 
        a = open(nomeArquivo, 'wt+') #open( ,write) - modo de escrita 
        a.close() #Sempre feche o arquivo para não deixá-lo aberto, mesmo depois de fechar o programa.
    except:
        print("Erro na criação do arquivo.")
    else: 
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')

def cadastrar_jogo(nomeArquivo, nome_jogo, console):
    try:
        a = open(nomeArquivo, 'at') #modo de escrita sem sobrescrever o conteúdo.
    except: 
        print('Erro ao abrir arquivo')
    else: 
        a.write(f'{nome_jogo}; {console}\n') # \n fará com que o programa use 'enter' para dar espaço.
    finally:
        a.close() #Garante que o arquivo seja fechado sempre.

def listarArquivo(nomeArquivo):
    try:
        a=open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

#PROGRAMA
arquivo = 'Parte5.2 - lista.txt'
if existe_arquivo(arquivo):
    print("Arquivo localizado no computador.")
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo)

while True:
    print('MENU')
    print("1 - Cadastrar novo item")
    print("2 - Listar cadastros")
    print("3 - Sair")
    op = valida_int('Escolha a opção desejada: ', 1, 3)

    if op == 1: #Cadastrar
        print('Opção de cadastrar selecionada...')
        nome_jogo = input("Digite o nome do jogo: ")
        console = input(f"Digite a qual console {nome_jogo} pertence: ")
        cadastrar_jogo(arquivo, nome_jogo, console)
    elif op ==2: #Listar
        print("Opção de listar selecionada...")
        listarArquivo(arquivo)
    elif op ==3: 
        print('Encerrando o programa...')
        break

