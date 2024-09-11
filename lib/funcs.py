import random

letrasUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letrasLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specials = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

def generar_letras(longitud: int):
    contra = ""
    for i in range(longitud):  # Ajustar en caso de querer cambiar la longitud :)
        se = random.choice(letrasLower) + random.choice(letrasUpper)
        contra += se # se de selection :v
    return contra

def generar_letras_y_numeros(longitud: int):
    all_chars = letrasUpper + letrasLower + nums
    contra = "".join(random.choice(all_chars) for _ in range(longitud))
    return contra

def generar_letras_numeros_y_especiales(longitud: int):
    all_chars = letrasUpper + letrasLower + nums + specials
    contra = "".join(random.choice(all_chars) for _ in range(longitud))
    return contra