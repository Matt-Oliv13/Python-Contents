'''
Laço 'for' (para)
# Para resolver problemas em que precisamos repetir determinadas linhas de código, assim como o laço while, porém para um número finito e bem definido de vezes.
'''

for i in range(4): #sendo i uma variável qualquer
    print(i) 
# Atenção! o valor entre parenteses corresponde ao "valor final a ser lido -1 ", pois o último valor nunca é lido pelo python no laço for. O primeiro valor, quano não definido, será sempre '0'. Os parenteses são obrigatórios!

# Podemos estabelecer parâmetros para manipular o looping do laço for. Para isso, ajustamos os itens nos parenteses da seguinte maneira: 
# for i in range(valor inicial de i, valor final de i, pulos de i):
for i in range (15, 240, 35):
    print(i) # assim, contamos do 15 ao 240 pulando de 35 em 35. Se os pulos forem omitidos, por padrão irá de 1 em 1.

frase = "Testando laço for"
for i in range(0, len(frase), 1): # No caso, como estamos usando len(frase), toda a frase será lida uma a uma.
    print(frase[i]) # exibe cada caractere i da frase
    #OBS: acrescente dentro do parênteses: ,end = "" 
    #Isso permite que os caracteres sejam impressos em uma mesma linha.


