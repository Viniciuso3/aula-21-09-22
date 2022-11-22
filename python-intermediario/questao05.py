list1 = []
list2 = []
list3 = []
print('*'*28)
print("_DIGITE 10 NUMEROS INTEIROS_")
print(' '*1)
for i in range(5):
    n = input('_Digite um numeros inteiros: ')
    list1.append(n)
    n2 = input('_Digite um numeros inteiros: ')
    list2.append(n2)
    list3 = list1 + list2 
    list3[::2] = list1 
    list3[1::2] = list2 
print (">> Os valores intercalados: " + str(list3)) 