# -*- coding: utf-8 -*-

def factorial(number):
    if number == 0:
        return 1
    
    return number * factorial( number - 1 )

if __name__ == '__main__':
    result = factorial(5)
    print('the result is: ')
    print(result)

