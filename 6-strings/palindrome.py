def palindrome2(s):
    reverse = s[::-1]
    
    if reverse == s:
        return True
    return False

def palindrome(s):
    reverse = []
    
    for letter in s:
        reverse.insert(0, letter)

    r = ''.join(reverse)

    if r == s:
        return True

    return False

if __name__ == '__main__':
    s = str(input('Type a word: '))

    result = palindrome2(s)

    if result is True:
        print('{} is palindrome!!!'.format(s))
    else:
        print('{} is not palindrome'.format(s))


