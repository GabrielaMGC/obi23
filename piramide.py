degraus = int(input("degraus: "))
k = 0
for i in range(1, degraus+1):
    for space in range(1, (degraus -i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ",end="")
        k += 1
    k = 0
    print()