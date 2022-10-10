dicionario = {
    "manha":"bom dia",
    "tarde":"boa tarde",
    "noite":"boa noite"
}

#print(dicionario["noite"])
    
nome=input('qual seu nome: ')
cpf=input('qual seu cpf: ')
endereco=input("qual seu endereco: ")
aniversario=input("qual seu aniversario: ")
rg=input("qual seu rg: ")

dados = {
    nome:'',
    cpf:"",
    endereco:"",
    aniversario:"",
    rg:''
}
#print(dados.items())'

tabela = {
    'nome': input('diga seu nome: '),
    'endereco': input('digite seu endereco: '),
    'aniversario': int(input('sua data de aniversario: ')),
    'cpf': int(input('digite seu cpf: ')),
    'rg': int(input('digite seu rg: '))
}

print(tabela)