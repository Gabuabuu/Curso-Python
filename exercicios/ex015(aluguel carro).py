dias = int(input('Quantos dias alugado?'))
km = float(input('Quantos km rodado?'))
totalPagar = (dias * 60 ) + (km * 0.15)
print(f'O total a pagar pela quantidade de {dias} alugado é de {totalPagar}!')