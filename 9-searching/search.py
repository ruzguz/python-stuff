def linear_search(list, element_to_search):
    for i in range(len(list)):
        if list[i] == element_to_search:
            return i
    
    return -1

def binary_search(list, element_to_search):
    i = 0
    j = len(list) - 1
    
    while i < j:
        k = (i+j) // 2
        if list[k] == element_to_search:
            return k
        elif list[k] > element_to_search:
            j = k - 1
        elif list[k] < element_to_search:
            i = k + 1
    return -1   
    
    


def run():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

    # linear search
    print(list)
    print('Linear search (1): {}'.format(linear_search(list, 1)))
    print('Linear search (49): {}'.format(linear_search(list, 49)))

    # binary search
    print('')
    print('Binary search (3): {}'.format(binary_search(list,3)))
    print('Binary search (35): {}'.format(binary_search(list,35)))

if __name__ == '__main__':
    run()
            
