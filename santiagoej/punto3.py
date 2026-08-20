class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_notas(self, n1, n2, n3):
        if all(0 <= n <= 100 for n in (n1, n2, n3)):
            self.notas = [n1, n2, n3]
        else:
            print("Las notas deben estar entre 0 y 100.")

    def calcular_promedio(self):
        if not self.notas:
            return 0
        return round(sum(self.notas) / len(self.notas))

    def estado_final(self):
        return "Aprobado" if self.calcular_promedio() >= 60 else "Reprobado"


# --- Uso del código ---
nombre = input("Nombre del estudiante: ")
alumno = Estudiante(nombre)

try:
    notas = [float(n.strip()) for n in input("Ingrese 3 notas separadas por coma: ").split(",")]
    if len(notas) == 3:
        alumno.agregar_notas(*notas)
        if alumno.notas:
            print(f"\nPromedio final de {alumno.nombre}: {alumno.calcular_promedio()}")
            print(f"Estado final: {alumno.estado_final()}")
    else:
        print("Debe ingresar exactamente 3 notas.")
except ValueError:
        print("Por favor, ingrese solo números válidos.")