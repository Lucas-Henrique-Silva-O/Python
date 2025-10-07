#Calculando a área de um triângulo com duas fórmulas

from math import pow

print('[1] - A = (b * h) / 2')
print('[2] - A = √((p - a) * (p -b) * (p - c)) onde p = ( a + b + c) / 2')
choice = int(input('Escolha qual das fórmulas você quer usar: '))

if choice == 1:
    b = float(input('Digite a base do triângulo em metros: '))
    h = float(input('Digite a altura do triângulo em metros: '))
    at = (b * h) / 2
    print(f'A área do triângulo de altura {h} e de base {b} é {at} m².')
elif choice == 2:
    a = float(input('Digite a medida do lado a: '))
    b = float(input('Digite a medida do lado b: '))
    c = float(input('Digite a medida do lado c: '))
    p = (a + b + c) / 2
    at = pow(p, 0.5)
    print(f'A área do triângulo {at} m².')




