def say_hello(age):
    if age >= 18:
        print('Hello sir')
    else:
        print('Hey kid')

def main():
    age = int(input('How old are you?: '))
    say_hello(age)

if __name__ == '__main__':
    main()
