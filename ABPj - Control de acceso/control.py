import json
import datetime

with open("usuarios.json", "r", encoding="utf-8") as archivo:
    usuarios = json.load(archivo)


def registrar_evento(mensaje):
    with open("auditoria.txt", "a", encoding="utf-8") as bitacora:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bitacora.write(fecha + " - " + mensaje + "\n")


while True:
    id_tarjeta = input("Ingrese gafete de empleado: ")

    if id_tarjeta.lower() == "salir":
        print("Sistema finalizado")
        break

    acceso = False

    for usuario in usuarios:
        if usuario["id_tarjeta"] == id_tarjeta:
            print("ACCESO PERMITIDO A PLANTA")
            registrar_evento(
                "ENTRADA AUTORIZADA - " + usuario["nombre_empleado"]
            )
            acceso = True
            break

    if not acceso:
        print("ALERTA DE SEGURIDAD")
        registrar_evento(
            "ALERTA - Intento de entrada NO AUTORIZADA"
        )

    print()