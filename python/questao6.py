print("<<< Retirando as letra a e A da frase >>> \nA casa do garoto tem algumas coisas legais.")
w1 = 'A casa do garoto tem algumas coisas legais.'
w2 = 'a,A'

for i in w2: 
    w1 = w1.replace(i, '')

print("<<<< A frase sem as letra a e A fica >>>> \n{}".format(w1)) 