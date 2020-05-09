def reverse(str):
    print(str[::-1])

def first(str):
    print(str[0])

def last(str):
    print(str[len(str)-1])

if __name__ == '__main__':
    s = input('Type something: ')
    
    first(s)
    last(s)
    reverse(s)

