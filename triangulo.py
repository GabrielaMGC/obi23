A = int(input())
B = int(input())
C = int(input())

lista = [A,B,C]
lista.sort()
maior = lista[2]
medio = lista[1]
menor = lista[0]
if menor + medio >= maior:
    print("S")
else:
    print("N")