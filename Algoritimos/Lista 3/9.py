meses = ['jan', 'fev', 'mar', 'a3br', 
         'mai', 'jun', 'jul', 'ago',
        'set', 'out', 'nov', 'dez']

num = int(input('digite um numero: '))

if num < 12:
    print(meses[num-1])
else: 
    print('n disponivel')