def numeros(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            print("Numero no valido, por favor ingresa un numero valido")


num1 = numeros("Ingresa un numero: ")
num2 = numeros("ingresa otro numero: ")
operacion = input("que operacion deseas realizar: ")

while operacion not in ["+", "-", "*", "/"]:
    print("No has elegido una opción válida, por favor intenta de nuevo") 
    operacion = input("¿Qué operación deseas realizar? ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2

print("el resultado es ", resultado)

