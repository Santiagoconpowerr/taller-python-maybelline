def buscar_clave_profunda(estructura, clave_objetivo):
    if isinstance(estructura, dict):
        if clave_objetivo in estructura:
            return estructura[clave_objetivo]
        for valor in estructura.values():
            resultado = buscar_clave_profunda(valor, clave_objetivo)
            if resultado is not None:
                return resultado
    return None


datos = {"a": 1, "b": {"c": 2, "d": {"e": 3, "objetivo": "encontrado"}}}
print(buscar_clave_profunda(datos, "objetivo"))
print(buscar_clave_profunda(datos, "inexistente"))
