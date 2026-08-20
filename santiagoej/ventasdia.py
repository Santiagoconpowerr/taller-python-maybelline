from collections import Counter

ventas_dia = [
    "Electrónica", "Ropa", "Electrónica", "Hogar",
    "Ropa", "Electrónica", "Juguetes", "Hogar"
]

conteo = Counter(ventas_dia)

categorias_unicas = set(ventas_dia)
categoria_mas_vendida = conteo.most_common(1)[0][0]

print("Categorías únicas:", categorias_unicas)
print("Cantidad de ventas:", dict(conteo))
print("Categoría más vendida:", categoria_mas_vendida)