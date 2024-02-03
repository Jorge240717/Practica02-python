from datetime import datetime
def convertir_fecha(fecha_input):
    formatos_entrada = ["%m/%d/%Y", "%B %d, %Y"]
    for formato in formatos_entrada:
        try:
            fecha_obj = datetime.strptime(fecha_input, formato)
            fecha_output = fecha_obj.strftime("%Y-%m-%d")
            print(f"Fecha en formato AAAA-MM-DD: {fecha_output}")
            break
        except ValueError:
            continue
    else:
        print("Formato de fecha no reconocido")
fecha_usuario = input("Ingrese una fecha (mes-día-año o mes día, año): ")
convertir_fecha(fecha_usuario)