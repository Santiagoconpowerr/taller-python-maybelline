def aplanar_lista(lista_anidada):
    resultado = []
    for elemento in lista_anidada:
        if isinstance(elemento, list):
            resultado.extend(aplanar_lista(elemento))
        else:
            resultado.append(elemento)
    return resultado


print(aplanar_lista([1, [2, [3, 4], 5], 6, [7]]))
