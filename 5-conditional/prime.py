def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % 1 == 0:
                return False
    return True

def run():
    number = int(input('Introduce a number: '))
    result = is_prime(number)

    if result is True:
        print('Is prime')
    else:
        print('Is not prime')

    print('')

if __name__ == '__main__':
    run()
