carteira = int(input('Saldo na carteira: '))
conversor = float(5.50)

disponivel = carteira * conversor

carteiraUSD = float(input('Saldo na carteira'))
real = float(5.50)

disponivelUSD = carteiraUSD * conversor

print(f'Você possui {carteira} e pode comprar US${round(disponivel, 2)} dolares')
print(f'Você possui {carteiraUSD} e pode comprar R${round(disponivelUSD, 2)} reais')