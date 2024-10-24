salario = input('Nome do protudo: ')
preco = float(input('Qual o preço do produto? '))
aumento = int(input('Valor do aumento: '))
novo = preco + (preco * aumento / 100)

print(f'O valor de {preco}R$ do Monitor agora tá por {round(novo, 2)}R$ com {aumento}% de aumento')

#ROUND() = Serve para arredondar um número para uma quantidade especifica de casas decimais