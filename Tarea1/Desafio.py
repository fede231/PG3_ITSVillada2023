desicion= input("queres hacer un cuadrado o un triangulo?")
if desicion=="cuadrado":
    print("dame un ancho")
    ancho = int(input(">>"))
    print("dame un alto")
    alto = int(input(">>"))
    print("dame un caracter")
    caracter = input(">>")

    for i in range(alto):
        for j in range(ancho):
            print(caracter, end=" ")
        print()
else:
        base = int(input("Ingresa la base del triángulo: "))
        caracter = input("Ingresa el carácter para el dibujo: ")
        for i in range(1, base + 1):
            print((caracter * i).rjust(base))

