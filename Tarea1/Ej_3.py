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
