'''
SOBRE FUNÇÕES
Funções são rotinas de códigos que podem ser executadas quando têm seu nome invocado dentro do programa. Ex: Print, input, int, range, etc.
* Parênteses são obrigatórios para funções
* estrutura: Palavra-chave + Nome da função + ( ) + :
(Lembre e while e for, o laço while é uma estrutura e por isso seus parenteses são opcionais, já o laço for é uma função, tendo os parênteses obrigatórios)
'''

# Vamos tentar criar uma função com base nessas linhas:

print('|','__' * 10,'|')
print('|','__' * 10,'|')
print('          MENU')
print('|','__' * 10,'|')
print('|','__' * 10,'|')

# Ao rodar o código, criamos uma espécie de área de menu com os prints. Agora vamos transformar esses tracejados em uma função reprodutível:

def realce(): # def é a função utilizada para definir outras funções.
  #corpo da função:
  print('|','__' * 10,'|')
  print('|','__' * 10,'|')

#Programa principal:
realce()
print('          MENU' )
realce()

#-------------------------------------------

# Definição de Parâmetros
# Parâmetros são dados recebidos pelas funções. O ato de enviar um dado para uma função é chamado de passagem de parâmetro. A variável que servirá de parâmetro irá dentro do parênteses obrigatório da função. Ex:

def realce(s1):
    print('|','__' * 10,'|')
    print('|','__' * 10,'|')
    print(s1)
    print('|','__' * 10,'|')
    print('|','__' * 10,'|')

realce('          MENU')
realce('          AMOR')
realce('         CÓDIGO')

#----------------------------------------
#Outro Exemplo:
def sub2(x,y):
   res = x - y
   print(res)

sub2(5,7)
sub2(8,2)
sub2(3,1)

#OBS: a ordem importa, mas você pode trocá-la se explicitar quais são os parâmetros. Ex: 

sub2(y=7, x=5)
#----------------------------------------

# Podemos também definir parâmetros opcionais para as funções, ex:

def sub3(x=0, y=0, z=0):
   res = x - y - z
   print(res)

sub3(3,2,1)
sub3(3,2) # z omitido
sub3(3) # y e z omitidos
sub3() # x, y e z omitidos

#--------------------------------------

# EXERCICIO PRÁTICO:
def borda(s1):
   tam=len(s1)
   #só imprime caso exista algum caractere.
   if tam:
      print('+', '-' * tam,'+')
      print('|',s1,'|')
      print('+','-' * tam,'+' )

borda('Olá, Mundo!')
borda('Deu certo, viu só? =D')

#-----------------------------------------

'''
Escopo de variáveis: É a propriedade que determina onde uma variável pode ser utilizada dentro de um programa. 

   * Escopo local - Criado sempre que a função é chamada. Variáveis criadas, seja no campo de parâmetro ou dentro do corpo da função fazem parte do escopo local daquela função e são chamadas de variáveis locais. Essas variáveis só existem dentro daquela própria função. Se trabalharmos com mais de uma função, cada uma usando uma variável de mesmo nome, essas variáveis NÃO se sobrescrevem, funcionando apenas dentro da própria função correspondente.

   * Escopo global - Criado no programa principal. Variáveis globais pertencem a um escopo global. Uma variável global existe também em todas as funções invocadas ao longo do programa (exceto no caso de haver uma variável local de mesmo nome, a qual irá sobreescrever a global localmente).
   
''' 
# Função:
def omelete():
   print(ovos) # escopo local
# Programa:
ovos = 12 #variável global
omelete() #função consegue usar a variável global.
# Se a variável estivesse no escopo local, o programa não conseguiria trabalhar com ela globalmente e geraria erro. 
# Atenção! Isso também vale para mais de uma função. Ex:
def omelete():
   ovos = 12
   bacon()
   print(ovos)

def bacon():
   ovos = 6

# Programa:
ovos = 2 #variável global
omelete() # Retorna 12, pois no contexto da função 'omelete' só existe a variável ovos = 12, sobrescrevendo a global. A variável na função bacon() NÃO SOBRESCREVE a variável de omelete(). Para que o 6 aparecesse, precisaríamos colocar um 'print(ovos)' dentro da função bacon() e mesmo assim teríamos como valores retornados: 6 e 12 (sem sobrescrever).

#-----------------------------

# Instrução Global - Força nosso programa a não criar uma variável local de mesmo nome e manipular somente a global dentro de uma função (sobrescrevendo-a globalmente!). Ex:

def omelete():
   global ovos
   ovos = 6
#programa:
ovos = 12
omelete() # A função mudou a variável globalmente, mas não tem um print associado.
print(ovos) # Aqui vamos printar fora do escopo local e ver que retorna 6.

# E como fica associando mais funções?
print("ex de instrução global")
def omelete():
   global ovos #Instrução global
   ovos = 6 #Aqui o valor da global (24) será alterado para 6.
   pimenta() #Chama a função pimenta()

def pimenta():
   ovos = 12 # variável no escopo local sem instrução global
   print(ovos) # 1º retorno: 12 (pela variável local)
   queijo() #Chama a função queijo

def queijo():
   print(ovos) #2º retorno: 6, pois a variável global 24 foi modificada para 6

#programa:
ovos = 24 #variável global
omelete() #chama a função omelete, que altera a global e chama a função pimenta()
print(ovos) #imprime o valor final da variável global alterada (6) 

#Resultado: 12 > 6 > 6

#OBS: 
'''
def omelete():
   print(presunto)
   presunto = 6

presunto = 12
omelete()

O programa retorna erro, pois a função omelete não pode imprimir a variável presunto sem que ela existe localmente, a menos que importemos a global com "global presunto" antes do print.
'''
#-------------------------------------------------

# Retorno de Valores (return) em Funções: 
# Diferenciação de Procedimento x Função:
   # Procedimento - rotina sem retorno
   # Função - rotina que retorna um dado a quem solicita

def soma3(x=0, y=0, z=0):
   res = x+y+z
   return res 
   #existe uma diferença importante entre print() e return: 
   #print apenas exibe o valor, enquanto return "devolve" o valor de dentro de uma função para ser manipulado fora dela.
resultado = soma3(5,3,2)
print(resultado)

def somaerro(x=0, y=0, z=0):
   res1 = x+y+z
resultado1 = somaerro(2,1,2)
print(resultado1) #Imprime "None", pois res1 não foi retornado para fora do escopo local.

#--------------------------------------------
#Exercício - Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo, e falso, caso contrário.


def valida_string(pergunta, min, max):
   s1 = input(pergunta) # "Digite uma string: " é a variável pergunta
   tam = len(s1)  # Essa variável local mede o nº de caracteres de s1
   while ((tam < min) or (tam>max)): # Estabelece a relação de menor ou maior e define um looping para continuar sendo executado enquanto não for escrito um input com o tamanho dentro do intervalo.
      s1 = input(pergunta) 
      tam = len(s1)
      # Aqui os parametros são novamente checados no looping
   return s1 # Retorna a string digitada ao término para ser usada fora da função.

x = valida_string("Digite uma string: ", 10, 30) # min e max definidos agora
print(f"você digitou a string {x}. \n Dado válido. Encerrando o programa...")

# -------------------------------------------------

'''
FUNCAO LAMBDA
É mais simples, sem nome, podendo ser escrita em uma só linha de código e dentro do programa principal. Ex:
'''
res = lambda x: x*x
print(res(3))

soma = lambda x,y: x + y
print(soma(2,3))

#Estrutura: 'lambda' + parâmetros + ':' + as variáveis dos parâmetros.

   


