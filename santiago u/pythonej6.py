def auditar_evento(nivel, *etiquetas, **metadatos):
    salida = f"[{nivel}]"
    if etiquetas:
        salida += " Tags: " + ", ".join(f"#{e}" for e in etiquetas)
    if metadatos:
        salida += " | Metadatos -> " + ", ".join(f"{k}: {v}" for k, v in metadatos.items())
    print(salida)


auditar_evento("ERROR", "seguridad", "auth", usuario="admin", ip="192.168.1.50", intento=3)
auditar_evento("INFO")
