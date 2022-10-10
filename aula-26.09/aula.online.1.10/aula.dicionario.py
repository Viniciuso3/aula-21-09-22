pessoas = {'nome': 'vinicius', 'sexo': 'm', 'idade': 18}
#pessoas['nome'] = 'jose'
#print(pessoas['idade'])
#print(f'o sexo do {pessoas["nome"]} e {pessoas["sexo"]}.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
for k in pessoas.keys():
   print(k)


for k in pessoas.values():
    print(k)


for k, v in pessoas.items():
    print(f'{k} = {v}')  


