def agregar_bitacora_bug(mensaje, historial=[]):
    historial.append(mensaje)
    return historial


print(agregar_bitacora_bug("Evento 1"))
print(agregar_bitacora_bug("Evento 2"))


def agregar_bitacora(mensaje, historial=None):
    if historial is None:
        historial = []
    historial.append(mensaje)
    return historial


print(agregar_bitacora("Evento 1"))
print(agregar_bitacora("Evento 2"))
