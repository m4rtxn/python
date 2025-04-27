
palabra = input("Ingresa una palabra")
#invertimos la palabra

def invertir_palabra(palabra):
    palabra_invertida= palabra[::-1]
    return palabra_invertida


def es_palindromo(palabra):
    return palabra ==invertir_palabra(palabra)

print(es_palindromo(palabra))