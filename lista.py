#quantidade = int(input())
#lista = []

#for i in range(quantidade):
 #  numero = int(input())
 #   lista.append(numero)

#print(lista)

#\n = quebra de linha

#dois valores em uma unica linha
#tamanho, numero = map(int, input().split())
#print(f'tamanho: {tamanho}\nnumero: {numero}')

#n valores em uma unica linha
#entrada = list(map(int, input().split()))
#print(entrada)

#print(sum(entrada))
#entrada.sort()
#print(entrada)

lista = []
quantidade = int(input())

for i in range(quantidade):
    cidade, pessoas = map(str, input().split())
    lista.append([cidade,pessoas])

print(lista)