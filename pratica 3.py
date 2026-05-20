#Exercicio (4) Um cinema cobra preços diferentes para os ingressos, de acordo com a idade da pessoa. Se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso custará R$ 15; se tiver mais de 12 anos, custará R$ 30. Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema. Encerre o laço, usando um break quando o usuário digitar 0. Após encerrar o laço, apresente na tela o total de pessoas que compraram os ingressos, o total de dinheiro arrecadado e a média das idades das pessoas.

total = 0
vendas = 0
cont = 0
total_idades = 0

while True:
    idade = int(input("Digite sua idade para comprar um ingresso, ou '0' para cancelar a operação: "))
    cont = cont + 1
    if idade == 0:
        break

    if idade < 3:
        preco = 0
        print("entrada gratuita")
 
    if idade >= 3 and idade <= 12:
        preco = 15
        print(f"o valor da entrada para sua idade é: R${preco}")
      
    if idade > 12:
        preco = 30
        print(f"o valor da entrada para sua idade é: R${preco}")
    
    vendas = vendas + 1
    total = total + preco
    total_idades = total_idades + idade
print(total_idades)
print(cont)

media_idades = total_idades / cont
print(f"o número de pessoas que compraram ingressos foi {vendas}")
print(f'o total de dinheiro arrecadado foi em R$ {total}')
print(f'a média das idades das pessoas foi: {media_idades}')