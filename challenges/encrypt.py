def encrypt(msg):
    # convert each character to binary number
    result = [ bin(ord(c)) for c in msg ]
    return ''.join(result)

def decrypt(msg):
    chars = msg.split('0b')
    # convert each binary number to character
    result = []
    for c in chars:
        if c != '':
            result.append(chr(int(c, 2)))
    return ''.join(result)

def run():
    while True:
        print('--- * --- * --- * --- * ---')
        print('Encryption app')
        print('[1] encrypt message')
        print('[2] decript message')
        print('[3] exit')
        print('--- * --- * --- * --- * ---')
        
        option = input('Select an option: ')

        if option == '1':
            msg = input('Introduce the message to encrypt: ')
            print('Encrypted message: {}'.format(encrypt(msg)))
        elif option == '2':
            msg = input('Introduce encryptes message: ')
            print('Decrypted message: {}'.format(decrypt(msg)))
        elif option == '3':
            break
        else:
            print('Invalid command')

if __name__ == '__main__':
    run()