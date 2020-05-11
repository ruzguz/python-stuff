def binary_search(list, element_to_find, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    
    if list[mid] == element_to_find:
        return mid
    elif list[mid] > element_to_find:
        return binary_search(list, element_to_find, start, mid - 1)
    elif list[mid] < element_to_find:
        return binary_search(list, element_to_find, mid + 1, end)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 12, 15, 23, 25, 28, 44]

    number_to_find = int(input('Introduce the number you wanna find: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) -1)

    print('The number is in the {} index'.format(result))


