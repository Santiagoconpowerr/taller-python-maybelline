def crear_perfil_usuario(nombre, email, rol):
    if "@" not in email:
        return "Error: el email no contiene el símbolo @"
    return {"nombre": nombre, "email": email, "rol": rol}


print(crear_perfil_usuario("Laura Gómez", "laura@empresa.com", "Desarrolladora"))
print(crear_perfil_usuario(rol="Admin", nombre="Carlos", email="carlos_sin_arroba"))
