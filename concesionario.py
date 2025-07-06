# -------------------------------------------------------------------------
# Ejercicio: Gestión de vehículos en un concesionario
# 
# 1. Clase Vehiculo con marca, modelo y precio privado.
#    Propiedad para el precio (getter y setter con control).
#    Método especial __str__.
# 2. Clases Coche y Moto que heredan de Vehiculo y añaden atributos.
# 3. Clase Concesionario para gestionar una lista de vehículos.
# 4. Programa principal: crea varios vehículos y muestra todos.
# -------------------------------------------------------------------------

class Vehiculo:
    def __init__(self, marca, modelo, precio):
        # Constructor: Inicializa los atributos de Vehiculo
        self.marca = marca           # Marca del vehículo (str)
        self.modelo = modelo         # Modelo del vehículo (str)
        self.precio = precio         # Usa el setter para validación

    @property
    def precio(self):
        # Getter para precio
        return self._precio

    @precio.setter
    def precio(self, valor):
        # Setter para precio con validación
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    def __str__(self):
        # Muestra la información básica del vehículo
        return f"{self.marca} {self.modelo} - Precio: {self.precio}€"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, precio, puertas):
        # Constructor de Coche: llama al constructor de Vehiculo
        super().__init__(marca, modelo, precio)
        self.puertas = puertas       # Número de puertas (int)

    def __str__(self):
        # Muestra la información del coche
        return f"{super().__str__()} - Puertas: {self.puertas}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio, tipo):
        # Constructor de Moto: llama al constructor de Vehiculo
        super().__init__(marca, modelo, precio)
        self.tipo = tipo             # Tipo de moto (str)

    def __str__(self):
        # Muestra la información de la moto
        return f"{super().__str__()} - Tipo: {self.tipo}"


class Concesionario:
    def __init__(self):
        # Constructor: inicializa la lista vacía de vehículos
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        # Añade un vehículo a la lista
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.marca} {vehiculo.modelo} añadido.")

    def mostrar_vehiculos(self):
        # Muestra todos los vehículos en el concesionario
        print("\n--- Listado de Vehículos ---")
        if not self.vehiculos:
            print("No hay vehículos en el concesionario.")
        for v in self.vehiculos:
            print(v)


# Programa principal
if __name__ == "__main__":
    concesionario = Concesionario()  # Crea el concesionario

    # Crea dos coches y dos motos (ejemplo)
    coche1 = Coche("Toyota", "Corolla", 18000, 5)
    coche2 = Coche("Seat", "Ibiza", 14000, 3)
    moto1 = Moto("Yamaha", "XMAX", 6000, "scooter")
    moto2 = Moto("Kawasaki", "Ninja", 12000, "deportiva")

    # Agrega los vehículos al concesionario
    concesionario.agregar_vehiculo(coche1)
    concesionario.agregar_vehiculo(coche2)
    concesionario.agregar_vehiculo(moto1)
    concesionario.agregar_vehiculo(moto2)

    # Muestra todos los vehículos
    concesionario.mostrar_vehiculos()
