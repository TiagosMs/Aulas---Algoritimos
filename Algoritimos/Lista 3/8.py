valor1 = int(input('numero 1 >> '))
valor2 = int(input('numero 2 >> '))

if valor1 and valor2 < 10:
    if valor1 + valor2 < 8:
        print('a media dos numeros {}'.format((valor1 + valor2) / 2))
    elif valor1 + valor2 == 8:
        print('o produto entros os numeros é {}'.format(valor2 * valor1))
    elif valor1 + valor1 > 8:
        print('a divisão entre os numero é {}'.format(valor1/valor2))
else:
    print('seu numero n é permitido')