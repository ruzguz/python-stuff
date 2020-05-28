def sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum(a + 1, b -1)
    elif b < 0:
        return sum(a - 1, b + 1)

if __name__ == '__main__':
    print('Welcome to the sum calculator')
    a = int(input('Introduce \'a\' value: '))
    b = int(input('Introduce \'b\' value: '))

    print(sum(a, b))
