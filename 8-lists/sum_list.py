def sum_elements(l):
    sum = 0

    for e in l:
        sum += e

    return sum

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    
    result = sum_elements(l)
    print('The sum of the elements is = {}'.format(result))

