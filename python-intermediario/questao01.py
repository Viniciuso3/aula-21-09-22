from re import A


print('_Bom dia_ \n_Os combustiveis desponiveis sao_\nA = alcool: \nG = gasolina:')
while True:
    t = input('_Qual o tipo de combustivel voce deseja: \n>> ')

    a = ('alcool')
    gasolina = ('G')


    if t == a:
        a = int(input('_Qual a quantidade de combustivel voce deseja: \n'))
        break
    else:
        print('tente novamente')
        break