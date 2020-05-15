VOWELS = 'AaEeIiOoUu'

def remove_vowels(str):
   return ''.join([c for c in str if c not in VOWELS])

if __name__ == '__main__':
    str = input('Type something: ')
    
    print(remove_vowels(str))
