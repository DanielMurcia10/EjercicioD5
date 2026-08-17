def mostrar_menu(): #funcion solo para almacenar el menu y despues mandar a llamar la funcion para no volver a escribir la funcion
    print("\t ------------- ")
    print("\t  CALCULADORA  ")
    print("\t ------------- \n")

    print("1. Suma (+) \n")
    print("2. Resta (-) \n")
    print("3. Multiplicacion (*) \n")
    print("4. Division (/) \n" )
    print("5. Mostrar historial \n")
    print("6. Salir... \n")



def pedir_datos(): # en esta funcion se procesan los datos que entran al programa 

    while True:
         dato = input("Ingrese un numero: ") #se guardan los datos que entran al sistema para despues validar si es un dato valido para realizar los calculos.

         if dato == " ":
            print("Error: no pueden haber campos vacios. ")
            continue #si se cumple la condicion, quiere decir que el valor ingresado es incorrecto
                     #y se vuelve a entrar al bucle para pedir otro dato hasta que la condicion no se cumpla

         try:
             numero = float(dato) #si el valor ingresado es correcto, este try/except no se ejecuta
         except ValueError:
              print("Error: eso no es un numero")
              continue

         
         return numero 
             


def ejecutar_calculadora():
    historial = []  #lista en donde se guardaran las operaciones que haga el usuario

    while True:   #bucle en donde se repetira el programa hasta salir del bucle 
        mostrar_menu()                               # se manda a llamar la funcion para mostrar las opciones del usuario
        opcion = input("Elige una opción: ")         # guarda la opcion del usuario 

        if opcion == "1":                            
            num1 = pedir_datos()                     # guarda el dato numero uno y se llama la funcion para validar si es un dato valido o no
            num2 = pedir_datos()                     # guarda el dato numero dos y se llama la funcion para validar si es un dato valido o no
            resultado = num1 + num2                  # realiza la operacion y la guarda en la variable resultado 
            operacion_texto = f"{num1} + {num2} = {resultado}"  # concatena las variables y junta el resultado para mostrar en pantalla un solo mensaje 
            historial.append(operacion_texto)        # agrega ese texto al final de la lista historial
            print("Resultado:", resultado)           # se usa append para agregar la operacion al historial

        elif opcion == "2":                          
            num1 = pedir_datos()
            num2 = pedir_datos()
            resultado = num1 - num2
            operacion_texto = f"{num1} - {num2} = {resultado}"
            historial.append(operacion_texto)
            print("Resultado:", resultado)

        elif opcion == "3":                          
            num1 = pedir_datos()
            num2 = pedir_datos()
            resultado = num1 * num2
            operacion_texto = f"{num1} * {num2} = {resultado}"
            historial.append(operacion_texto)
            print("Resultado:", resultado)

        elif opcion == "4":                         
            num1 = pedir_datos()
            num2 = pedir_datos()

            if num2 == 0:                             # se evalua si el divisor es = 0 
                print("Error: no se puede dividir entre cero")
                continue                               # regresa al bucle para y no sigue con el proceso

            resultado = num1 / num2
            operacion_texto = f"{num1} / {num2} = {resultado}"
            historial.append(operacion_texto)
            print("Resultado:", resultado)

        elif opcion == "5":                          
            if len(historial) == 0:                   #se usa len para medir la logitud del historial y se confirma si es igual a 0, y si es = 0 es porque aun no hay operaciones guardadas
                print("Aún no hay operaciones")
            else:
                for operacion in historial:            # recorro cada elemento guardado en la lista y se declara "operacion" para guardar el resultado de la busqueda para despues mostrarlo en pantalla
                    print(operacion)                   

        elif opcion == "6":                           
            print("¡Hasta luego!")
            break                                       # sale del bucle y finaliza el programa 

        else:                                          # cualquier otra cosa que no sea "1" al "6"
            print("Opción inválida, intenta de nuevo")


ejecutar_calculadora() #se escribe afuera de una funcion para poder ejecutar el programa