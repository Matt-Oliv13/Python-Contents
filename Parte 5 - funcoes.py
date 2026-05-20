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