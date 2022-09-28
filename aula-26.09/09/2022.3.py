while True:
    n1 = input('qual seu nome: ') 
    n2 = input('qual seu sobrenome: ')
    produto = [n1 + n2]
    print(produto)

    n3 = input('qual seu nome: ')
    n4 = input('qual seu sobrenome: ')
    resultado = [n3 + n4]
    print(resultado)

    n5 = input('qual seu nome: ')
    n6 = input('qual seu sobrenome: ')
    valor = [n5 + n6]
    print(valor)

    s = (produto + resultado + valor)
    print(s) 
    print('lista finalizada')
    break
    
    