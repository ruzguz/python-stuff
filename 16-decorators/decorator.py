def protected(func):
    
    def wrapper(password):
        if password == '1234':
            return func(password)
        else:
            print('Access denied')

    return wrapper

def token(func):
    
    def wrapper(password):
        print('this is your access token : {}sdf8a0f8090809sa8df098098as0df980'.format(password))
    
    return wrapper


@protected
@token
def protected_function():
    print('Access granted')

if __name__ == '__main__':
    password = input('Introduce the password: ')
    protected_function(password)