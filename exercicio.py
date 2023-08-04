entrada = list(map(int, input().split()))

entrada.sort()
menor = entrada[0]

entrada.sort(reverse = True)
maior = entrada[0]

print(f'menor: {menor}\nmaior: {maior}')