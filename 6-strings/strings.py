def print_letter_by_letter(string):
    for i in range(len(string)):
        print('[{}] - {}'.format(i,string[i]))

if __name__ == '__main__':
    phrase = input('Type something: ')
    print_letter_by_letter(phrase)
