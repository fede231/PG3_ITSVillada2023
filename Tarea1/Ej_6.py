frase = input("dame una palabra: ")

def contar (frase):
    contador = 0
    for letra in frase:
        if letra in "aeiou":
            contador += 1

    if contador > 0:
        print(f"tenes {contador} vocales.")
    else:
        print("no tenes vocales.")

contar(frase)