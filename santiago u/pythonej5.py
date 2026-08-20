def calcular_metricas(*numeros, **opciones):
    operacion = opciones.get("operacion", "suma")
    if operacion == "promedio":
        resultado = sum(numeros) / len(numeros)
    else:
        resultado = sum(numeros)
    redondear = opciones.get("redondear", False)
    if redondear:
        decimales = redondear if isinstance(redondear, int) and not isinstance(redondear, bool) else 0
        resultado = round(resultado, decimales)
    return resultado


print(calcular_metricas(1, 2, 3, 4, operacion="promedio"))
print(calcular_metricas(1, 2, 3, 4, operacion="suma"))
print(calcular_metricas(1.5, 2.333, 3.777, operacion="promedio", redondear=2))
