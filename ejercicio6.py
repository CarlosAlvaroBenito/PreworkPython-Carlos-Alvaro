'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''


def es_palindroma(texto):
    palabras = texto.split()
    palindromos = []

    for palabra in palabras:
        palabra = palabra.lower()
        if palabra == palabra[::-1]:
            palindromos.append(palabra)

    return palindromos

texto = input("Ingrese una frase: ")
resultado = es_palindroma(texto)
print("Palabras palindrómicas encontradas:", resultado)