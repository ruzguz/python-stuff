def count_spaces(str):
    return len([c for c in str if c == ' '])

if __name__ == '__main__':
    str = input('Type something: ')

    print(count_spaces(str))
    print('')

