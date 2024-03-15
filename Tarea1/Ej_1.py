lista = [1, 2, 3, 4, 5, 6]
print ("Que elemento queres buscar?")
print (lista)
buscar = int(input(">>"))
def encontrar(buscar, lista):
    if buscar in lista:
        print ("Tu numero esta en la posicion", lista.index(buscar))
    else:
        (print ("No esta en la lista"))

encontrar(buscar, lista)