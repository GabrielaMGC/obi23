N = int(input())

V = []

for i in range(N):  
    E, A, G = map(str, input().split())
    A = float(A)
    G = float(G)
    if A <= G * 0.7:
        V.append(E)
    
if len(V) == 0:
    print(f'*')
else:
    for E in V:
        print(E)