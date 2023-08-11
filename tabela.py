J, P, V, E, D = map(int, input().split())

if J == -1:
   J = V + E + D 
if P == -1:
   P = 3 * V + E
if V == -1:
   V = J - (E + D)
if E == -1:
   E = J - (V + D)
if D == -1:
   D = J - (V + E)

print(f'{J} {P} {V} {E} {D}')