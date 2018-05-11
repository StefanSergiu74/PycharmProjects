def prim(num):
    contador = 0
    for i in range(2, num):
        for x in  range(2, i):
            if(i % x) == 0:
               # print(i, 'equals', x, '*', i // x)

                break

        else:
            contador += 1
            print(i, "is prime")

    print('In first', num, 'numbers are ', contador, 'prime numbers')
prim(78)



