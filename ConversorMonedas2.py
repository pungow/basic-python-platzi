
menu = '''
Bienvenido al  conversor de monedas 👍

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:
'''

def coversor(tipo_pesos, valor_dolar):
    pesos = float(input(f'Cuantos pesos {tipo_pesos} tienes?: '))
    dolares = pesos / valor_dolar
    dolares = str(round(dolares, 2))
    print(f'tienes {dolares} USD')

while(True):
    opcion = int(input(menu))
    if opcion == 1:
        coversor('Colombianos', 3700)
    elif opcion == 2:
        coversor('Argentinos', 56)
    elif opcion == 3:
        coversor('Mexicanos', 24)
    else:
        print('Ingrese una opcion correcta')