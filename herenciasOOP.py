# Definimos la clase base Animal
class Animal:
    # Método constructor con nombre y edad
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad      # Atributo edad

    # Método genérico que puede ser sobreescrito por subclases
    def hablar(self):
        pass  # No hace nada aquí, se espera que subclases lo definan

    # Método que describe al animal
    def describir(self):
        return f"{self.nombre} tiene {self.edad} años."  # Devuelve descripción del animal

# Clase Perro hereda de Animal
class Perro(Animal):
    # Sobrescribe el método hablar
    def hablar(self):
        return "¡Guau!"  # Sonido típico de un perro

# Clase Gato también hereda de Animal
class Gato(Animal):
    # Sobrescribe el método hablar
    def hablar(self):
        return "Miau..."  # Sonido típico de un gato

# Clase extra que NO hereda de Animal, pero se usará en herencia múltiple
class MascotaInteligente:
    # Método que muestra una habilidad de mascota inteligente
    def saludar(self):
        return f"Hola, soy {self.nombre} y puedo aprender trucos 🧠"

# Clase que hereda de Gato Y de MascotaInteligente (herencia múltiple)
class GatoRobot(Gato, MascotaInteligente):
    # Método adicional exclusivo de GatoRobot
    def cargar(self):
        return "🔋 Cargando baterías..."

# Bloque principal que solo se ejecuta si este archivo es ejecutado directamente
if __name__ == "__main__":
    # Creamos un objeto Perro
    perro = Perro("Toby", 4)

    # Creamos un objeto Gato
    gato = Gato("Luna", 3)

    # Creamos un objeto GatoRobot, que hereda de Gato y MascotaInteligente
    robogato = GatoRobot("MichiBot", 2)

    # Mostramos descripción y sonido del perro
    print(perro.describir(), perro.hablar())

    # Mostramos descripción y sonido del gato
    print(gato.describir(), gato.hablar())

    # Mostramos descripción, sonido, saludo y estado de batería del GatoRobot
    print(robogato.describir(), robogato.hablar(), robogato.saludar(), robogato.cargar())
