'''
Nessa aula veremos sobre o comando de entrada (INPUT)
Sempre começamos atribuindo uma variável com a função 'input()' - exibido ao usuário
Ex:
'''
idade = input("Qual a sua idade? ")
print(f'Sua resposta, {idade} anos, foi registrada!')
'''
CASTING DE VARIÁVEIS:
'Problema do Input': Ele sempre devolve os dados no tipo 'String'. Sendo assim, se eu desejo realizar
operações númericas após a inserção dos dados no input, precisarei converter a variável para 'int' ou 
'float' antes do input
'''
nota = float(input('Defina um valor para multiplicar por 4 ')) #Sem isso, o próximo passo retornaria TypeError
print(nota *4/2) 
'''
-----------------
FLUXO DE EXECUÇÃO DE PROGRAMAS:
'''
x=1
y=1
z=x+y #z=2
x=x+2 #x=1+2=3
y=y-1 #y=1-1=0
z=x+y #z=3+0=3
print(f'o valor final das variáveis se tornou: {x}, {y}, {z}')