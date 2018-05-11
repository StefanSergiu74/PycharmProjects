def oddEven(list):
    odd = []
    even = []
    while len(list) > 0:
        number = list.pop()
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    print('The even list: ', even)
    print('The odd list: ', odd)


lista = [1, 34, 43, 22, 36, 21, 4, 45, 56, 16, 85, 93, 82]
print(oddEven(lista))
