
numeros = (input("dame numeros separados por espacio sin un orden:"))
lista = numeros.split()
lista = [int(numero) for numero in lista]
lista.sort(reverse=True)

print(lista)