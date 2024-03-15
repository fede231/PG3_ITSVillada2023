numero = int(input("dame numeros sin separar: "))
def es_numero_step(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        digito_actual = int(numero_str[i])
        digito_siguiente = int(numero_str[i + 1])
        
        if abs(digito_actual - digito_siguiente) != 1:
            print("no es step") 
        else:
            print("es step")       
es_numero_step(numero)