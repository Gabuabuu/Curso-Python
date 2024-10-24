produto = input('Nome do protudo: ')
preco = float(input('Qual o preço do produto? '))
desconto = int(input('Valor do desconto: '))
novo = preco - (preco * desconto / 100)

print(f'O valor de {preco}R$ do Monitor agora tá por {novo}R$ com 5% de desconto')