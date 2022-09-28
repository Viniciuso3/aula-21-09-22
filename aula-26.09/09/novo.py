def par(n):
    return (n%2 == 0)
print(par(9))


def hello(nome):
    print('ola, mestre')
print(hello('vinicius'))


def mult(x, num=2):
    return x, x*num

a,b = mult(2)
print(a,b)

a,b = mult(2, num=10)
print(a,b)

a,b = mult(3, 5)
print(a,b)


def soma  (n1, n2, n3):
    n1 = int(input('digte um numero: '))
    n2 = int(input('digete outro numero: '))
    n3 = int(input('digit outro numero: '))
    produto = n1 + n2 + n3 
    print(produto)
print(soma(1,2,3))

