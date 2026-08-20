def inicializar_db(host, puerto, db_name, usuario, password):
    return f"Conectando a {db_name} en {host}:{puerto} como {usuario}"


config = {
    "host": "cluster-db.internal",
    "puerto": 5432,
    "db_name": "production_v2",
    "usuario": "app_user",
    "password": "S3cur3P@ss!"
}

print(inicializar_db(**config))
