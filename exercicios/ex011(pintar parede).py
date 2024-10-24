largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura

print(f'Sua parede tem uma dimensão de {largura}x{altura} e sua área é de {area}m²')

tinta = area / 2

print(f'Para pintar essa parede voce precisará de {tinta}l de tinta')