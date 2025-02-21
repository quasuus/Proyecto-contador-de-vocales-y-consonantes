def contar_vocales(frase):
    vocales= 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    return sum(1 for letra in frase if letra in vocales) #función para contar las vocales

def contar_consonantes(frase):
    consonantes= 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for letra in frase if letra in consonantes) #función para contar las consonantes

def contar_palabras(frase):
    return len(frase.split()) if frase.strip() else 0 #función para contar palabras

total_vocales= 0
total_consonantes= 0 #variables a las que se le asignaran valores después
total_palabras= 0


while True:
    frase=input("Ingresa una frase: ") #menú para ingresar frase
    if not frase:
        break 


    while True:
        print("\nMenú")
        print("1. Contar vocales")
        print("2. Contar consonantes") #menú interactivo
        print("3. Contar palabras")
        print("4. Salir")

        opción = input("Elige la opción: ")

        if opción == '1':
            num_vocales= contar_vocales(frase)
            total_vocales+= num_vocales
            print(f"Vocales en la frase: {num_vocales} \nTotal acumulado: {total_vocales}") #primera opción del menú
        elif opción == '2':
            num_consonantes= contar_consonantes(frase)
            total_consonantes+= num_consonantes
            print(f"Consonantes en la frase: {num_consonantes} \nTotal acumulado: {total_consonantes}")#segunda opción del menú
        elif opción == '3':
            num_palabras= contar_palabras(frase)
            total_palabras+= num_palabras
            print(f"Palabras en la frase: {num_palabras} \nTotal acumulado: {total_palabras}")#tercera opción del menú
        elif opción == '4':
            print(f"Saliendo... \nEstadisticas finales: \nTotal Vocales: {total_vocales} \nTotal Consonantes: {total_consonantes} \nTotal Palabras: {total_palabras}")#cuarta opción del menú
            break
        else:
            print("Opción no válida, intenta de nuevo.")