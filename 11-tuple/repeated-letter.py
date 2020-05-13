# example strings
str1 = 'aabbabcbbabd'
str2 = 'ccffghhmmkkls'
str3 = 'oopeedfsksk'

def find_not_repeated_char(str):

    for letter in str:
        if str.count(letter) == 1:
            return letter

    return 'All letters are repeated'
        

if __name__ == '__main__':
    str = input('Type something: ')
    print('')
    print('-----------examples---------')
    print('{} : {}'.format(str1, find_not_repeated_char(str1)))
    print('{} : {}'.format(str2, find_not_repeated_char(str2)))
    print('{} : {}'.format(str3, find_not_repeated_char(str3)))
    print('-----------------------------')
    print('{} : {}'.format(str, find_not_repeated_char(str)))
