# calculator to use basics operators

# sum
def sum(a, b):
    return a + b

# subtraction 
def sub(a,b):
    return a - b

# multiplication
def mult(a,b):
    return a * b

# division
def div(a,b):
    return a / b

# main funciton
def main():
    print('Welcome to the calculator, select an option:')
    print('1 - sum')
    print('2 - subtraction')
    print('3 - multiplication')
    print('4 - division')

    option = int(input(''))
   
    a = int(input('Introduce a: '))
    b = int(input('Introduce b: '))

    if ( option == 1 ):
        print(sum(a,b))

    if ( option == 2 ):
        print(sub(a,b))

    if ( option == 3 ):
        print(mult(a,b))

    if ( option == 4 ):
        print(div(a,b))

if __name__ == '__main__':
    main()
