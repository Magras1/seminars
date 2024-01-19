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

4.19)
print([[2, 4, -2, -3, 0 , 11 , 3 -1][i] if [2, 4, -2, -3, 0 , 11 , 3 -1][i] >= 0 else i for i in range(len([2, 4, -2, -3, 0 , 11 , 3 -1]))])

5.1)  
def pr(a: int or float, b: int or float) -> int or float:
    return a * b
print(pr(int(input('a = ')), int(input('b = '))))

5.2)
def pr(a: int or float, b: int or float = 1, c: int or float = 1) -> int or float:
    return a * b * c
print(pr(2))
print(pr(2, 5))
print(pr(2, 3, 54))

5.3)
print(pr(*(15, 10 ,5)))
print(pr(*(3, 1)))
print(pr(*[2, 35, 55]))
print(pr(*(5, 10 ,15, 20)[:3]))
print(pr(*(5, 10 ,15, 20)[1:4]))

5.4)
def pr(*a) -> int or float:
    k = 1
    for i in a:
        k *= i
    return k
print(pr(*(15, 10 ,5)))
print(pr(*(3, 1)))
print(pr(*[2, 35, 55]))
print(pr(*(5, 10 ,15, 20)[:3]))
print(pr(*(5, 10 ,15, 20)[1:4]))

5.5)
def pro(k):
    if k == '*':
        return 10 * 5  
    elif k == '-':
        return 10 - 5
    elif k == '+':
        return 10 + 5
    elif k == '/':
        return 10 // 5
print(pro(input()))

5.6)
def calc(op):
    if op.find('-') != -1:
        return int(op.split(' - ')[0]) - int(op.split(' - ')[1])
    elif op.find('*') != -1:
        return int(op.split(' * ')[0]) * int(op.split(' * ')[1])
    elif op.find('+') != -1:
        return int(op.split(' + ')[0]) + int(op.split(' + ')[1])
    elif op.find('/') != -1:
        return int(op.split(' / ')[0]) // int(op.split(' / ')[1])
    elif op.find('%') != -1:
        return int(op.split(' % ')[0]) % int(op.split(' % ')[1])
    elif op.find('^') != -1:
        return int(op.split(' ^ ')[0]) ** int(op.split(' ^ ')[1])
print(calc(input()))


    


