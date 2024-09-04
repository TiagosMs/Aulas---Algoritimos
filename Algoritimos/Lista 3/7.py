x = int(input('coordenada x >> '))
y = int(input('coordenada y >> '))

if x > 0 and y > 0:
    print('primeiro quadrante')
if x < 0 and y > 0:
    print('segundo quadrante')
if x > 0 and y < 0:
    print('quarto quadrante')
if x < 0 and y < 0:
    print('terceiro quadrante')