def avg_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += temp
    
    return sum_of_temps / len(temps)


if __name__ == '__main__':
    temps = [21,24,22,20,23,24]

    avg = avg_temps(temps)

    print('The average temperatures is: {}'.format(avg))

