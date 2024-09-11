from lib import generar_letras, generar_letras_y_numeros, generar_letras_numeros_y_especiales

print("-----------------\n¡Bienvenido!\nEste es un generador de contraseñas seguras.\nPulsa [Enter] para continuar")
input()

print("Selecciona el tipo de contraseña que deseas generar:")
print("1. Solo letras (mayúsculas y minúsculas)")
print("2. Letras y números")
print("3. Letras, números y caracteres especiales")

def question():
    opcion = input("Introduce el número de la opción deseada: ")
    
    try:
        longitud = int(input("Introduce la longitud de la contraseña: "))
    except ValueError:
        print("Error: Debes introducir un número para la longitud.")
        return None  

    if opcion == '1':
        contraseña = generar_letras(longitud)
    elif opcion == '2':
        contraseña = generar_letras_y_numeros(longitud)
    elif opcion == '3':
        contraseña = generar_letras_numeros_y_especiales(longitud)
    else:
        print("Opción no válida, por favor elige 1, 2 o 3.")
        return None 
    
    return contraseña 

contraseña = None
while contraseña is None:
    try:
        contraseña = question() 
    except ValueError:
        print("Error, introduce un valor válido. Inténtalo de nuevo.")

if contraseña:
    print(f"\nTu contraseña segura es: {contraseña}")
