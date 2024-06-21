class EntidadTiempo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}:"


class Ciudad(EntidadTiempo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.registros = []

    def agregar_registro(self, tipo, temperatura):
        self.registros.append((tipo, temperatura))

    def promedio_temperaturas(self):
        if not self.registros:
            return 0
        suma_temperaturas = sum(temperatura for _, temperatura in self.registros)
        return suma_temperaturas / len(self.registros)


class Semana(EntidadTiempo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.ciudades = []

    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad)


def crear_datos_ejemplo():
    ciudades_nombres = ["Tena", "Puyo", "Salcedo", "El Coca", "Quito", "Shushufinfi"]

    # Datos de ejemplo de temperaturas para tres semanas
    temperaturas_semanas = [
        [19, 16, 20, 15, 18, 22],
        [24, 24, 21, 16, 17, 23],
        [18, 26, 22, 14, 19, 24]
    ]

    semanas = []

    for semana_num, temperaturas in enumerate(temperaturas_semanas, start=1):
        semana = Semana(f"Semana {semana_num}")
        for nombre_ciudad, temperatura in zip(ciudades_nombres, temperaturas):
            tipo = "temperatura"  # Se mantiene el tipo como 'temperatura'
            ciudad = Ciudad(nombre_ciudad)
            ciudad.agregar_registro(tipo, temperatura)
            semana.agregar_ciudad(ciudad)
        semanas.append(semana)

    return semanas


def calcular_temperatura_promedio_semanal(ciudad_nombre, datos):
    num_semanas = len(datos)
    suma_temperatura = 0
    num_registros = 0

    for semana in datos:
        for semana_ciudad in semana.ciudades:
            if semana_ciudad.nombre.lower() == ciudad_nombre.lower():
                suma_temperatura += semana_ciudad.promedio_temperaturas()
                num_registros += 1
                break  # Salir del bucle interior una vez que se encuentra la ciudad

    if num_registros == 0:
        raise ValueError(f"No se encontraron registros para la ciudad '{ciudad_nombre}' en los datos proporcionados.")

    promedio_semanal = suma_temperatura / num_registros
    return promedio_semanal


# Crear datos de ejemplo
datos = crear_datos_ejemplo()

# Solicitar ciudad al usuario
ciudad_nombre = input("Ingrese el nombre de la ciudad para calcular el promedio de temperaturas: ")

try:
    promedio_semanal = calcular_temperatura_promedio_semanal(ciudad_nombre, datos)
    print(f"El promedio de temperatura semanal para la ciudad de {ciudad_nombre} es: {promedio_semanal:.2f} grados")
except ValueError as e:
    print(f"Error: {e}")