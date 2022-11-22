n = int(input("_Digite um numero: \n"))
n1, n2 = 1, 1
contador = 0 
while contador < n:
    n3 = n1 + n2
    if n3 == n:
        print('_Termo encontado:')
        break
    elif n3 != n:
        print("_Termo nao encontrado:")
        break
    