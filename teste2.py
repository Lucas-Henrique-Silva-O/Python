#Calculando o quadrado da soma de dois termos e o quadrado da diferença de dois termos
import math

a = float(input('Digite o primeiro termo: '))
b = float(input('Digite o segundo termo: '))

quadrado_da_soma = (a+b) ** (2)
quadrado_da_diferenca = (a - b) ** (2)
qs = math.pow((a+b), 2)
qd = math.pow((a-b), 2)
print(f'({a})² + 2 *{a} * {b} + ({b})²')
print(f'({a})² - 2 * {a} * {b} + ({b})²')
print(f'{math.pow(a, 2)} + 2 * {a} * {b} + {math.pow(b, 2)} = {qs}')
print(f'{math.pow(a, 2)} - 2 * {a} * {b} + {math.pow(b ,2)} = {qd}')
print(f'O resultado de ({a} + {b}) é {quadrado_da_soma}')
print(f'O resultado de ({a} - {b}) é {quadrado_da_diferenca}')
print(qs)
print(qd)



