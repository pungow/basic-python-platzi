import random


def digit():
    number = int(input('Write number 0-10: '))
    return number


def run():
    number_random = random.randint(0, 100)
    number = digit()
    while number != number_random:
        if number < number_random:
            print('the number is less 🠕🠕🠕')
        else:
            print('the number is greater 🠗🠗🠗')
        number = digit()
    print('you guessed the number')


if __name__ == '__main__':
    run()