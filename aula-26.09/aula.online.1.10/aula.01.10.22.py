#n1 = int(input('digite um numero inteiro: '))
#s = n1 + 1
#d = n1 - 1
#print('analisando o valo {}, seu antecessor e {}, e seu sucessor e {}'. format(n1, d, s))


#n = int(input('degite um valor inteiro: '))
#print('analisando o valo {}, seu antecessor e {}, e seu sucessor e {}'. format(n, (n-1), (n+1)))



#lista = [2,4,6,8,10]
#nova = [ x*x for x in lista ]
#rint (nova)
lista = [2,3,6,7,8,9,10,11]
nova = []
for x in lista:
    if (x%2)==0:
        nova.append(str(x))
#print (nova)

lista= [2,3,6,7,8,9,10,11]
nova = [str(x) for x in lista if (x%2==0)]
#print(nova)

texto = "There is someone in my head but it is not me ".split()
nova = [(p.upper(),
len(p))
for p in texto]
#print(nova)

import os
from glob import glob
files = [f for f in glob('*.py')]
#print(files)


class ponto:
    pass
p = ponto()
#print(p)

#contrutor:
class ponto:
    def __init__(self, x ,y):
        self.xcoord = x
        self.ycoord = y

p = ponto(2.0, 1.0)
print(p)