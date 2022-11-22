list = [10,11,20,22,30,33,40,44,50,55,60,66,70,77,80,88,90,99]
listapar = []
listaimpa =[]

for c in list:
    if c % 2==0:
        listapar.append(c)
    else:
        listaimpa.append(c)

print('_Na lista abaixo imprima os numeros pares e os numeros impares_ \n{}'.format(list))
print('_PARES_')
print(listapar)

print('_IMPARES_')
print(listaimpa)
