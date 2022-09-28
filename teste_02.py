
from re import A


while True:
    A = int(input('digite uma nota de 0 a 10: '))
    if A >= 0 and A <= 10:
        break
    print("numero invalido")
