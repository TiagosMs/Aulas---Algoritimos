# TEM JEITO MUUUITO MAIS FACIL DE FAZER USANDO ARRAYS

#PAIS 1
pais1 = input('pais 1: ')
ouro1 = int(input('ouro: '))
prata1 = int(input('prata: '))
bronze1 = int(input('bronza: '))

a = (ouro1 * 3) + (prata1 * 2) + (bronze1)

#PAIS 2
pais2 = input('pais 2: ')
ouro2 = int(input('ouro: '))
prata2 = int(input('prata: '))
bronze2 = int(input('bronza: '))

b = (ouro2 * 3) + (prata2 * 2) + (bronze2)

#PAIS 3
pais3 = input('pais 3: ')
ouro3 = int(input('ouro: '))
prata3 = int(input('prata: '))
bronze3 = int(input('bronza: '))

c = (ouro3 * 3) + (prata3 * 2) + (bronze3)

#APURAÇÃO DA CLASSIFICAÇÃO

primeiro = 0
segundo = 0
terceiro = 0

if a > b and a > c:
    primeiro = a
    print(pais1)
    if b > c:
        segundo = b
        print(pais2)
        terceiro = c
        print(pais3)
    else:
        segundo = c
        terceiro = b
elif b > a and b > c:
    primeiro = b
    print(pais2)
    if a > c:
        segundo = a
        print(pais1)
        terceiro = c
        print(pais3)
    else:
        segundo = c
        print(pais3)
        terceiro = a
        print(pais1)
else:
    primeiro = c
    print(pais3)
    if a > b:
        segundo = a
        print(pais1)
        terceiro = b
        print(pais2)
    else:
        segundo = b
        print(pais2)
        terceiro = a
        print(pais1)