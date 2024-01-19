4.13)
print([len(i) for i in ['1', '123', '123', '12', '1', '123']])

4.14)
print(len([i for i in ['1', '123', '123', '12', '1', '123'] if len(i) > 2]))

4.15)
print(sum([i * k for i, k in {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}.items()]))

4.16)
d7 = {i: k for i, k in {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}.items() if i not in {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}}

4.17)
list_1 = [i * k for i, k in enumerate([2, 4, -2, -3, 0 , 11 , 3 -1])]
print(list_1)

4.18)

print([i if i >= 0 else '' for i in [2, 4, -2, -3, 0 , 11 , 3 -1]])
