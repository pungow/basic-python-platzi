def run():
    for count in range(100):
        if count % 2 != 0:
            continue
        print(count)
    for i in range(1000):
        if i == 500:
            break
        print(i)
    text = input('Write a text: ')
    for letter in text:
        if letter == 'o':
            break
        print(letter)



if __name__ == '__main__':
    run()