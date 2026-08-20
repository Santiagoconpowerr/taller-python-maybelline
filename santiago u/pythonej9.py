def procesar_coleccion(lista_datos, funcion_transformacion, funcion_filtro):
    resultado = []
    for dato in lista_datos:
        if funcion_filtro(dato):
            resultado.append(funcion_transformacion(dato))
    return resultado


es_par = lambda x: x % 2 == 0
duplicar = lambda x: x * 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(procesar_coleccion(numeros, duplicar, es_par))
