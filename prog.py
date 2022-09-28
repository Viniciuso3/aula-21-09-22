n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valo: '))
opcao = 0
while opcao != 5:
    print(''' [1]somar
[2]multiplica
[3]dividir
[4]subtrair ''')
    break
opcao = int(input(">>>>>qual a sua opcao? "))
if opcao == 1:
        produto = [n1 + n2]
        print('o resultado de {} + {} e {}'.format(n1, n2, produto))
elif opcao == 2: 
    produto1 = [n1 * n2]
    print('o resultado de {} x {} e{}'.format(n1, n2, produto1))
elif opcao == 3:
    produto2 = [n1/n2]
    print('o resultado de {} / {} e {}'.format(n1, n2, produto2))
elif opcao == 4:
    produto3 = [n1-n2] 
    print('o resultado de {} - {} e {}'.format(n1, n2, produto3))
elif opcao == 5:
    print('sair da conta: ')   
else:
    print('opcao invalida:')
    