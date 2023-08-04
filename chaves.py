linhas = int(input())
textoTotal = ''
for i in range(linhas):
    textLinha = str(input())
    textoTotal += textLinha
abriu = 0
fechou = 0
for caracter in textoTotal:
    if caracter == "{":
        abriu += 1
    if caracter == "}":
        abriu -= 1
        fechou += 1
if abriu == 0:
    print("S")
else:
    print("N")