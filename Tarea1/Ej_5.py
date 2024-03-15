print("dame una palabra")
palabra = input(">>")
reves = palabra[::-1]
def palindromo(palabra, reves):
    if palabra==reves:
        True
        print("es palindromo")
    else:
        False
        print("no es palindromo")
palindromo(palabra, reves)