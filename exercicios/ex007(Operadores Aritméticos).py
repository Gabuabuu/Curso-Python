n1 = float(input('Digite sua media no primeiro trimestre'))
n2 = float(input('Digite sua media no segundo trimestre'))

resultado = (n1 + n2) / 2

if resultado >= 6:
    print('Aprovado')
elif resultado <= 5:
    print('Reprovado')
else:
    print('Aprovado')

print(round(resultado, 1))

#ROUND() serve para arredondar um valor, o numero depois da virgula indica a quantidade de casas decimais

