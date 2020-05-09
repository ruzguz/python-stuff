import random

def run():
    number_found = False

    # generating random range from user input 
    min = int(input('Introduce the min value: '))

    max = int(input('Introduce the max value: '))

    while max <= min:
        max = int(input('max value have to be greater than min value: '))


    random_number = random.randint(min, max)


    while not number_found:
        number = int(input('Try: '))
        if number == random_number:
            print('Congratulation, you rock!!!')
            number_found = True
        elif number < min or number > max:
            print('number out of range >:(')
        elif number >  random_number:
            print('<')
        elif number < random_number:
            print('>')
        

if __name__ == '__main__':
    run()

