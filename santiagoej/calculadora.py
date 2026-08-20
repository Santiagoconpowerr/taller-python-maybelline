nombre_cliente = input("Nombre del cliente: ")
precio_base = float(input("Precio base del producto: "))
cantidad = int(input("Cantidad adquirida: "))
es_vip = input("¿El cliente tiene membresía? (s/n): ").strip().lower() == 's'

total_sin_descuento = precio_base * cantidad
cumple_cantidad = cantidad >= 5

if cumple_cantidad and es_vip:
    descuento_volumen = 0.25
elif cumple_cantidad or es_vip:
    descuento_volumen = 0.15
else:
    descuento_volumen = 0.0

monto_descuento = total_sin_descuento * descuento_volumen
total_final = total_sin_descuento - monto_descuento

print("\n--- RESUMEN DE COMPRA ---")
print(f"Cliente: {nombre_cliente}")
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Descuento aplicado: {int(descuento_volumen * 100)}%")
print(f"Monto descontado: ${monto_descuento:.2f}")
print(f"Total a pagar: ${total_final:.2f}")