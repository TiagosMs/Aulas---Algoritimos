funcionario = int(input('qual o seu codigo: '))
salario = int(input('qual o seu salario: '))


if funcionario == 1:
    salario = salario * (50/100) + salario
    print (salario)
elif funcionario == 2:
    salario = salario * (30/100) + salario
    print (salario)
elif funcionario == 3:
    salario = salario * (20/100) + salario
    print (salario)