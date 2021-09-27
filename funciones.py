'''
def imprimir_msj():
    print('Mensaje espcial')
    print('Esoty aprendiendo')

imprimir_msj() '''
'''
def conversacion(mensaje):
    print('Hola')
    print('Como estas?')
    print(mensaje)
    print('adios')

opcion = int(input('Elige una opcion 1, 2, 3:'))

if opcion == 1:
    conversacion('elegiste la opcion 1')
elif opcion == 2:
    conversacion('elegiste la opcion 2')
elif opcion == 3:
    conversacion('elegiste la opcion 3')
else:
    print('escribe una opcion correcta')'''

def suma(a, b):
    resultado = a + b
    return resultado
sumatoria = suma(4, 6)
print(sumatoria)