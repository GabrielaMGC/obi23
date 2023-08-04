N = int(input())
R = int(input())
P = int(input())

dias = 0
ia = N

while ia<P:
    dias+=1
    ni = N*R
    N = ni
    ia += N

print(dias)