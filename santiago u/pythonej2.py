def aplicar_impuesto(tasa_iva, lista_precios):
    print(tasa_iva, lista_precios)
    for i in range(len(lista_precios)):
        lista_precios[i] = round(lista_precios[i] * (1 + tasa_iva), 2)
    tasa_iva = tasa_iva + 0.05
    print(tasa_iva, lista_precios)


tasa_iva = 0.19
lista_precios = [100, 200, 300]
aplicar_impuesto(tasa_iva, lista_precios)
print(tasa_iva, lista_precios)
