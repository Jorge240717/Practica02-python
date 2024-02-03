def omitir_vocales(cadena):
    cadena_sin_vocales = ''.join(char for char in cadena if char.lower() not in {'a', 'e', 'i', 'o', 'u'})
    return cadena_sin_vocales
cadena_usuario = input("Ingrese una cadena de texto: ")
resultado = omitir_vocales(cadena_usuario)
print(f"Texto sin vocales: {resultado}")