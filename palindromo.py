def palindromo(palabra):
    palabra = palabra.replace(' ', '').upper()
    if palabra == palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindrome = palindromo(palabra)
    if es_palindrome == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    while True:
        run()