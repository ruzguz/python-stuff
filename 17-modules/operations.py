import mathf

def print_menu():
    print('1 - sum')
    print('2 - subtraction')
    print('3 - multiplication')
    print('4 - square number')
    print('5 - division')

if __name__ == '__main__':
    while True:
        print('Welcome to the calculator:')
        print_menu()
        
        option = input('Select an option: ')

        if option == '1':
            a = int(input('Introduce \'a\' value: '))
            b = int(input('Introduce \'b\' value: '))
            print(mathf.sum(a, b))
        elif option == '2':
            a = int(input('Introduce \'a\' value: '))
            b = int(input('introduce \'b\' value: '))
            print(mathf.subtraction(a, b))
        elif option == '3':
            a = int(input('Introduce \'a\' value: '))
            b = int(input('Introduce \'b\' value: '))
            print(mathf.mult(a, b))
        elif option == '4':
            a = int(input('Introduce a number: '))
            print(mathf.square(a))
        elif option == '5':
            a = int(input('Introduce \'a\' value: '))
            b = int(input('Introduce \'b\' value: '))
            print(mathf.division(a, b))
        else:
            break
    

