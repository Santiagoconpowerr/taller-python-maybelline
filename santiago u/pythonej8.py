def generar_reporte(titulo, *secciones, **firmas):
    print(titulo)
    for s in secciones:
        print(s)
    for k, v in firmas.items():
        print(k, v)


secciones_basicas = ("Introducción", "Desarrollo")
secciones_adicionales = ["Conclusiones", "Anexos"]
firmas = {"autor": "Santiago", "revisor": "Ana"}

generar_reporte("Reporte Final", *secciones_basicas, *secciones_adicionales, **firmas)
