def dividir(a, b):
    if b == 0:
        return "Error"
    return a / b

if __name__ == "__main__":
    try:
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        print("Resultado:", dividir(a, b))
    except ValueError:
        print("Valores erroneos")
    except ZeroDivisionError:
        print("No ingresar el cero")