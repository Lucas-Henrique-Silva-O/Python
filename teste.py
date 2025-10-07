# Calculando raízes de equações quadráticas

print('Digite os valores das constantes da equação:')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b ** 2) - (4 * a * c)
r1 = (-b + (delta ** (0.5))) / (2 * a)
r2 = (-b - (delta ** (0.5))) / (2 * a)
print(f'Raiz um: {r1} e Raiz dois: {r2}')

if delta == 0:
    print('As raízes reais são iguais.')
elif delta < 0:
    print('Não há raízes reais para essa equação.')
else:
    print('As raízes reais são distintas.')


# Calculando o x e o y do vértice
xv = -b / (2* a)
yv = -delta / (4  * a)
print(f'As coordenadas do vértice são: ({xv}, {yv}).')
if a > 0:
    print('A concavidade da parábola é voltada para cima.')
else:
    print('A concavidade da parábola é voltada para baixo.')




