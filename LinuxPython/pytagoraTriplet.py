answer = 0
for c in range(1000,3,-1):
    for b in range(c-1,2,-1):
        a = 1000 - (c + b)
        if c**2 == (a**2 + b**2) and c :

            answer = a*b*c

print(answer)