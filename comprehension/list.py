def find_div_by_7(list):
    return [n for n in list if n % 7 == 0]

if __name__ == '__main__':
    print(find_div_by_7(range(0,1000)))
    print('')

