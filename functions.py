def soma(n1, n2):
    return n1 + n2

y = soma(10, 30)
print(f'A soma é {y}')

def fibonacci(n):
    return Nule

def pa(a0, n, razao):
    an = a0
    sequencia = list()
    sequencia.append(a0)
    for i in range(n):
        an += razao
        sequencia.append(an)
    return sequencia

t = pa(3, 10, 3)
print(f'A sequência da P.A. de a0 = 3 e razão 3 é: {t}')
cont = 0
while cont <= (len(t) - 1):
    print(f'{cont+1}º {t[cont]}')
    cont += 1

def pa1(t1, r, numero):
    seq = list()
    for k in range(numero):
        k = k + 1 # To correct the difference between the values
        tn = t1 + ((k - 1) * r)
        seq.append(tn)
    return seq

def total(quantity):
    p = 1
    total = 0
    while p <= quantity:
        n = int(input('Digite um número inteiro para o somatório: '))
        total += n
        p += 1
    return total

h = pa1(2, 2, 20)
print(f'A sequência da P.A. de a1 = 2 e razão 2 é: {h}')
for u in h:
    print(f'{u}')

print('-'*10)
soma = total(4)
print(soma)