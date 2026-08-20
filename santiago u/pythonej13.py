class EventDispatcher:
    def __init__(self, detener_en_error=False):
        self.listeners = {}
        self.detener_en_error = detener_en_error

    def registrar(self, evento, callback):
        if evento not in self.listeners:
            self.listeners[evento] = []
        self.listeners[evento].append(callback)

    def limpiar_payload(self, payload):
        if isinstance(payload, dict):
            return {k: self.limpiar_payload(v) for k, v in payload.items()}
        if isinstance(payload, list):
            return [self.limpiar_payload(v) for v in payload]
        if isinstance(payload, str):
            return payload.strip()
        return payload

    def emitir(self, evento, **payload):
        payload_limpio = self.limpiar_payload(payload)
        for callback in self.listeners.get(evento, []):
            try:
                callback(**payload_limpio)
            except Exception as e:
                if self.detener_en_error:
                    raise e


def on_login(usuario, ip):
    print(f"Usuario {usuario} inició sesión desde {ip}")


dispatcher = EventDispatcher(detener_en_error=False)
dispatcher.registrar("login", on_login)
dispatcher.emitir("login", usuario="  santiago  ", ip=" 192.168.1.10 ")
