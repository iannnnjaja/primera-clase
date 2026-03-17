import math

def factorial(n)
    if n < 0
        return "no existe factorial para numeros negativos"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def interes_compuesto(capital, tasa, tiempo):
    return capital * (1 + tasa) ** tiempo

def menu():
    print("---menu---")
    print("1. factorial")
    print("2. interes compuesto")
    print("3. salir")
    try:
        opcion = int(input("ingrese una opcion"))
        return opcion
    except ValueError
        print("entrada invalida. ingrese un numero")
        return 0 
    
    while True:
        choice = menu()
        if choice == 1
            try:
                numero = int(input("ingrese un numero: "))
                print("el factorial de", numero, "es", factorial(numero))
            except ValueError
                print("entrada invalida. Use numeros validos")
        elif choice == 3
            print("gracias por usar el programa")
            break
        else:
            print("opcion invalida")
        print("\n")