def run():
    numbers = [1, 43, 5, 6, 90]
    objects = ['Hello', 3, 4, True, 89.2]
    objects.append(False)
    objects.pop(2)
    for element in objects:
        print(element)

    print(objects[::-1])
if __name__ == '__main__':
    run()