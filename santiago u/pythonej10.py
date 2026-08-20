def ejecutar_mision(nombre_tarea, al_exito=None, al_error=None):
    try:
        if nombre_tarea == "":
            raise ValueError("Nombre de tarea vacío")
        resultado = f"Misión {nombre_tarea} completada"
        if al_exito:
            al_exito(nombre_tarea, resultado)
    except Exception as e:
        if al_error:
            al_error(nombre_tarea, str(e))


def manejar_exito(tarea, resultado):
    print(f"[EXITO] {tarea}: {resultado}")


def manejar_error(tarea, error):
    print(f"[ERROR] {tarea}: {error}")


ejecutar_mision("Despliegue", al_exito=manejar_exito, al_error=manejar_error)
ejecutar_mision("", al_exito=manejar_exito, al_error=manejar_error)
