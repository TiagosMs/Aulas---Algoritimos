num = int(input('digite um numero: '))

if num <= 10 and num > 0:
    print('seu numero esta entre 0 e 10')
elif num > 10 and num <= 100:
    print('seu numero esta entre 10 e 100')
elif num > 100 and num <= 1000:
    print('seu numero esta entre 100 e 1000')
elif num > 1000 and num <= 10000:
    print('seu numero esta entre 1000 e 10000')
else:
    print('seu numero n pertece a nenhum dos grupos')