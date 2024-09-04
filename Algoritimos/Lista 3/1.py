a = int(input('numero 1: '))
b = int(input('numero 2: '))
c = int(input('numero 3: '))

delta = b**2 - (4*a*c)

x = (-b + (delta**0.5))/2*a

if delta == 0:
    print('exite apenas uma solução')
