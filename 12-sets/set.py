def remove_item(s, item):
    s.remove(item)
    return s

if __name__ == '__main__':
    s = set(['php', 'c++', 'c', 'python', 'java'])

    print(s)
    print('')

    item = input('Type the element you\'d like to remove: ')

    print(remove_item(s, item))

