numeros_ingresados = []
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    if respuesta.upper() != "SI":
        break
    try:
        numero = int(input("Ingrese el número: "))
        numeros_ingresados.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")
print("Números ingresados:", numeros_ingresados)
numeros_pares = sum(1 for num in numeros_ingresados if num % 2 == 0)
numeros_impares = len(numeros_ingresados) - numeros_pares
print(f"\nCantidad de números pares: {numeros_pares}")
print(f"Cantidad de números impares: {numeros_impares}")
