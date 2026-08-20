def conectar_api(url, timeout=30, retries=3, use_ssl=True):
    protocolo = "https" if use_ssl else "http"
    return f"CONNECT {protocolo}://{url} --timeout={timeout} --retries={retries}"


print(conectar_api("api.miservicio.com"))
print(conectar_api("api.miservicio.com", timeout=10, use_ssl=False))
