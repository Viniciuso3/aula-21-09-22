brasil = []
estado = {'uf': 'ceara', 'sigla': 'ce'}
estado1 = {'uf': 'sao paulo', 'sigla': ' sp'}
brasil.append(estado)
brasil.append(estado1)

#print(estado)
#print(brasil)
#print(brasil[0])
#print(brasil[0] ['uf'])
#print(brasil[1] ['sigla'])



estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
#for da lista
for e in brasil:
#for dicionario
    for k, v in e.items():
        print(f'o campo {k} tem como valor {v}.')
