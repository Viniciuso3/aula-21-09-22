while True:
    n1 = input( 'qual seu nome: ')
    n2 = input('qual seu sobrenome: ') 
    resultado = [n1 + n2]
    print(resultado)

    n3 = input('qual seu nome: ')
    n4 = input('qual seu sobrenome: ')
    produto = [n3 + n4]
    print(produto)
    
    s = [resultado + produto]
    print(s)
    
    print('lista finalizada')
    break
   
    