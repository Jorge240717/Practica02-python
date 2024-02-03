def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():  
            inicio = ord('a') if caracter.islower() else ord('A')
            resultado += chr((ord(caracter) - inicio + desplazamiento) % 26 + inicio)
        else:
            resultado += caracter
    return resultado
texto_original = input("Ingrese el texto a cifrar: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print(f"Texto cifrado: {texto_cifrado}")
