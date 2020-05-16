def write(str):
    with open('newfile.txt', 'a') as f:
        f.write(str + '\n')

if __name__ == '__main__':
    str = input('Type something: ')

    write(str)
