from math import factorial


def is_prime(number):
    count = 0
    '''
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False
    '''
    for i in range(1, number):
        result = factorial(number-1) + 1
        if result % number == 0:
            return True
        else:
            return False


def run():
    number = int(input('write a number: '))
    if is_prime(number):
        print('is a prime number')
    else:
        print('it is not a prime number')


if __name__ == '__main__':
    while True:
        run()