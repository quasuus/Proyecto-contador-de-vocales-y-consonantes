def contar_vocales(frase):
    vocales= 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    return sum(1 for letra in frase if letra in vocales)

def contar_consonantes(frase):
    consonantes= 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for letra in frase if letra in consonantes)

def contar_palabras(frase):
    return len(frase.split()) if frase.strip() else 0

total_vocales= 0
total_consonantes= 0
total_palabras= 0


while True:
    frase=input("Ingresa una frase: ")
    if not frase:
        continue 


    while True:
        print("\nMenú")
        print("1. Contar vocales")
        print("2. Contar consonantes")
        print("3. Contar palabras")
        print("4. Salir")

        opción = input("Elige la opción: ")

        if opción == '1':
            num_vocales= contar_vocales(frase)
            total_vocales+= num_vocales
            print(f"Vocales en la frase: {num_vocales} \nTotal acumulado: {total_vocales}")
        elif opción == '2':
            num_consonantes= contar_consonantes(frase)
            total_consonantes+= num_consonantes
            print(f"Consonantes en la frase: {num_consonantes} \nTotal acumulado: {total_consonantes}")
        elif opción == '3':
            num_palabras= contar_palabras(frase)
            total_palabras+= num_palabras
            print(f"Palabras en la frase: {num_palabras} \nTotal acumulado: {total_palabras}")
        elif opción == '4':
            print(f"Saliendo... \nEstadisticas finales: \nTotal Vocales: {total_vocales} \nTotal Consonantes: {total_consonantes} \nTotal Palabras: {total_palabras}")
            break
        else:
            print("Opción no válida, intenta de nuevo.")