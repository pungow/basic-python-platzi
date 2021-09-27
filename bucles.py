
def run():
    # potencia de 2^n  n=(0,999)
    LIMITE = 1000
    for n in range(LIMITE):
        potencia = 2 ** n
        print(f'2 ^ {n} = {potencia}')
    #Ciclo while
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(f'2 ^ {contador} = {potencia_2}')
        contador = contador + 1
        potencia_2 = 2 ** contador
    #Ciclo For
    for contador in range(1, 1001):
        print(contador)
    #recorrer string
    nombre = input('write your name: ')
    for letra in nombre:
        print(f'{letra}')


if __name__ == '__main__':
    run()