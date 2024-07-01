# Conversor de Unidades de Medida
# Este programa convierte unidades de medida comunes: metros a kilómetros, gramos a kilogramos y Celsius a Fahrenheit
# Utiliza varios tipos de datos: integer, float, string, boolean

def convertir_metros_a_kilometros(metros: float) -> float:
    """Convierte metros a kilómetros."""
    return metros / 1000


def convertir_gramos_a_kilogramos(gramos: float) -> float:
    """Convierte gramos a kilogramos."""
    return gramos / 1000


def convertir_celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


def convertidor():
    print("Conversor de Unidades de Medida")

    while True:
        print("\nSelecciona la conversión que deseas realizar:")
        print("1. Metros a Kilómetros")
        print("2. Gramos a Kilogramos")
        print("3. Celsius a Fahrenheit")
        print("4. Salir")

        opcion = input("Ingresa el número de la opción deseada: ")

        if opcion == "1":
            metros = float(input("Ingresa la cantidad en metros: "))
            kilometros = convertir_metros_a_kilometros(metros)
            print(f"{metros} metros son {kilometros:.2f} kilómetros.")

        elif opcion == "2":
            gramos = float(input("Ingresa la cantidad en gramos: "))
            kilogramos = convertir_gramos_a_kilogramos(gramos)
            print(f"{gramos} gramos son {kilogramos:.2f} kilogramos.")

        elif opcion == "3":
            celsius = float(input("Ingresa la temperatura en grados Celsius: "))
            fahrenheit = convertir_celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")

        elif opcion == "4":
            print("Saliendo del conversor. ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    convertidor()