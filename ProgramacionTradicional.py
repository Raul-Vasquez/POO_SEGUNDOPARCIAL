# Programación Tradicional
# Ejemplo: Gestión de un vehículo

# Definición de variables globales
tanque_lleno = 0
mileage = 0
fuel_efficiency = 25

# Función para llenar el tanque de combustible
def fill_tank(amount):
    global tanque_lleno
    tanque_lleno += amount

# Función para conducir el vehículo
def drive(distance):
    global tanque_lleno, mileage, fuel_efficiency
    fuel_needed = distance / fuel_efficiency
    if fuel_needed <= tanque_lleno:
        tanque_lleno -= fuel_needed
        mileage += distance
        print("Recorrido:", distance, "miles")
    else:
        print("Not enough fuel to drive that far.")

# Uso de las funciones en la programación tradicional
fill_tank(20)
drive(100)

# Imprimir la distancia recorrida y el nivel de combustible restante
print("Kilometros (Traditional):", mileage)
print("Tanque LLeno (Traditional):", tanque_lleno)