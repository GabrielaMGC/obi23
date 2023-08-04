P = int(input())
D = int(input())
B = int(input())

if P*1+D*2+B*3 >= 150:
    print("B")
elif P*1+D*2+B*3 >= 120:
    print("D")
elif P*1+D*2+B*3 >= 100:
    print("P")
else:
    print("N")