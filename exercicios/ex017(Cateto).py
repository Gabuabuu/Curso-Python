from math import hypot
num1 = float(input('Comprimento do cateto oposto:'))
num2 = float(input('Comprimento do cateto adjacente:'))
hip = hypot (num1, num2)
print(f'A hipotenusa vai medir {hip:.2f}.')