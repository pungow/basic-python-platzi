valor_conversion = 0
while(1):
    opcion = input(' 1-COP a USD\n 2-USD a COP\n Digite su opcion: ')
    opcion_correcta = True
    if opcion == '1':
        valor_conversion = 3686

    elif opcion == '2':
        valor_conversion = 0.00027

    else:
        print('Digite un valor correcto')
        opcion_correcta = False

    if opcion_correcta == True:
        valor1 = float((input('¿Cuantos COP tienes?:')))
        valor2 = valor1 / valor_conversion
        valor2 = str(round(valor2, 3))
        print(f'El valor {valor1} es aquivalente a {valor2}\n')

