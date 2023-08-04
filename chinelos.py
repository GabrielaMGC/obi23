N = int(input())

qpt = []

for i in range(N):
    qpt.append(int(input()))
P = int(input())
pa = 0
for j in range(P):
    ap = int(input())
    t = qpt[ap-1]
    if t > 0:
        qpt[ap-1]-=1
        pa+=1

print(pa)