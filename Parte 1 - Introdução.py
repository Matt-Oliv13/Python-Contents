'''
Conceituando Dado, Variável e seus tipos:
Um dado é uma sequência de símbolos quantificável ou quantificáveis; valores fornecidos 
via entrada, que ficam salvos e podem ser manipulados ao longo do programa. Já uma variável 
é um nome dado à uma região da memória do programa, e sempre que for convocado, seu bloco
de memória é carregado automaticamente da RAM.

Resumo: Cada dado fica endereçado na memória por um código binário extenso;
A variável atribui um nome à esse bloco de código e toda vez que a chamamos, esse pedaço
da memória é acessado e carregado. 

OBS: REGRAS DO PYTHON PARA VARIÁVEIS
* Nunca inicie o nome de uma variável com algarismos. Ex: 2nota
* Nunca inicie o nome de uma variável com caractere especial, EXCETO underline '_'. Ex: _nota
* Acostume-se a separar nomes compostos de variaveis com "_". Ex: 'preco_total' e não 'precoTotal' 

RECOMENDAÇÕES!
* Apesar do 'ç' ser aceito no python 3, outras linguagens não aceitam a utilização, por isso não use.
* Verifique o conjunto oficial de regras do python https://peps.python.org/pep-0008/ 

TIPOS PRIMITIVOS DE DADOS:

*Númerico (Inteiro e ponto flutuante)
    -Para realizar operações aritméticas.
    -Inteiro (int): números sem cadas decimais.
    -Ponto flutuante (float): números com casas decimais.

*Literal/Booleana (ou variável lógica) (Bool)
    -A variável é usada para dois estados: 1 ou 0 / True or False / Nível lógico alto ou baixo
    -Operadores lógicos para comparação entre valores:
        == Comparação de igualdade (Não confunda com 1 sinal de '=' que é uma atribuição de valor)
        > Maior que
        < Menor que
        >= Maior ou igual a
        <= Menor ou igual a
        != Diferente de

*Caractere(Strings)
    -Armazenam conjuntos de símbolos encadeados, inclusive pontuação, acentuação e números 
    -ATENÇÃO! INDICES DOS CARACTERES: 
                Número inteiro que indica onde o caractere está dentro de uma string
                A contagem do indice sempre começa em zero
                Ex:
                Olá, Mundo - Conteúdo
                0123456789 - Índice
'''
test_indice = 'Testando indices'
print(test_indice[7], test_indice[12], test_indice[15]) #Retorna o i s
# Caso eu queira pegar mais de um caractere de uma vez, em sequência:
print(test_indice[0:7]) # Perceba que aqui estamos indo do caractere 0 ao 7. Mas o python nunca mostra o último caractere.
print(test_indice[0:8]) #Então precisamos sempre definir o caractere final como o último+1
print(test_indice[:8]) #Alternativamente, pode-se omitir o inicio para pegar todos os caracteres até o último definido

'''
CONCATENAÇÃO DE STRINGS
'''
s1 = "Primeira etapa para"
print(s1 + "entender Concatenação") # Perceba que aqui as palavras são juntadas sem um espaço para separá-las.
print(s1, "entender Concatenação") # Vírgula, diferentemente do '+', já pressupõe um espaço para serparar os elementos.
#Outro caso:
print("A" + "-" *30 + "B") # Assim, o Python multiplica a string "-" 30x
print("A" + " " *30 + "B") # Assim, o Python multiplica a string " " (espaço) 30x
'''
-----DIFERENTES MÉTODOS DE COMPOSIÇÕES COM VARIÁVEIS E STRINGS------
1) ANTIGO / RELACIONADO À LINGUAGEM C:
    -usar '%d' ou '%i' para nº inteiros, '%f' para decimais e '%s' para strings, diretamente na string e indicar
     a(s) variável(is) posterior(es) à '%' (em ordem). 
     Ex: 
'''
nota = 8.5
disciplina = 'Matemática'
v1 = 'Você tirou %.2f em %s' % (nota, disciplina) #obs: o '2' entre % e f é apenas para que tenhamos só 2 casas decimais!
print(v1) 
'''
2) COMPOSIÇÃO MODERNA:
    -ao invés de usar %, usaremos a seguinte estrutura: '{}' na string e '.format(variavel, variavel)' após ela
    Ex:
'''
v1 = 'Você tirou {} em {}'.format(nota, disciplina) 
print(v1) 
'''
3) COMPOSIÇÃO MAIS ATUAL/USUAL/OTIMIZADA:
    uso de f' antes da string e {} dentro dela. 
    Ex: 
'''
v1 = f'Você tirou {nota} em {disciplina}' 
print(v1) 
'''
-------------------------------------------------------------------------------
TAMANHO (length)
Podemos descobrir o tamanho de uma cadeia de caracteres com a função len.
Ex:
'''
palavra = "Oitenta e dois mil, setecentos e quatro"
numero_de_caracteres = len(palavra)
print(numero_de_caracteres)

'''
Aqui encerramos a aula introdutória com a noção de como funcionam os comandos de Saída!
'''