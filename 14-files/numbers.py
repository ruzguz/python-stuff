def run():
    with open('numbers.txt', 'w') as f:
        for i in range(30):
            f.write(str(i))


if __name__ == '__main__':
    run()

