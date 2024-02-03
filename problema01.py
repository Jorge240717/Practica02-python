resultados = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        resultados.append(num)
print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(resultados)