def contar_digitos(numero, digito):
    numero_str = str(numero)
    digito_str = str(digito)
    cantidad = numero_str.count(digito_str)
    print(f"Número ingresado: {numero}")
    print(f"Dígito a contar: {digito}")
    print(f"Cantidad de veces {digito} en el número: {cantidad}")
numero_ingresado = int(input("Ingrese un número entero: "))
digito_ingresado = int(input("Ingrese el dígito que desea contar: "))
contar_digitos(numero_ingresado, digito_ingresado)