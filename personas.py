# ---------------------------------------------------------------
# Ejercicios básicos de Clases y Objetos en Python
# Incluye: clase Persona, métodos, valores por defecto, __str__,
# clase Grupo, herencia con Estudiante, métodos de clase/estáticos,
# contador de instancias, propiedad edad, y composición con Coche.
# ---------------------------------------------------------------

# EJERCICIO 1: Definiendo una clase simple

class Persona:
    # El constructor inicializa los atributos de la persona
    def __init__(self, nombre, edad, ciudad="Desconocida"):
        self.nombre = nombre             # Almacena el nombre (str)
        self._edad = edad                # Edad (int), se guarda privada para el setter/getter
        self.ciudad = ciudad             # Ciudad (str), valor por defecto "Desconocida"

        # Contador de instancias: se incrementa al crear una persona
        Persona.contador_personas += 1

    # EJERCICIO 9: Propiedad getter y setter para edad
    @property
    def edad(self):
        return self._edad  # Devuelve la edad

    @edad.setter
    def edad(self, valor):
        # Controla que la edad no sea negativa
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor

    # EJERCICIO 1 y 4: Método presentarse y __str__
    def presentarse(self):
        # Muestra una presentación amigable
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}")

    def __str__(self):
        # Permite imprimir el objeto mostrando presentación
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}"

    # EJERCICIO 2: Método para incrementar edad
    def cumplir_anios(self):
        # Suma un año a la edad y lo muestra
        self.edad += 1
        print(f"Ahora tengo {self.edad} años.")

    # EJERCICIO 8: Contador de instancias como atributo de clase
    contador_personas = 0  # Se inicializa fuera de los métodos

# EJERCICIO 5: Clase con lista de objetos

class Grupo:
    # Constructor que crea una lista vacía de personas
    def __init__(self):
        self.personas = []  # Lista para almacenar objetos Persona

    def agregar_persona(self, persona):
        # Añade una persona al grupo
        self.personas.append(persona)

    def mostrar_personas(self):
        # Presenta a todas las personas del grupo
        print("Personas en el grupo:")
        for persona in self.personas:
            print(persona)  # Se usa __str__ de Persona

# EJERCICIO 6 y 7: Herencia y métodos de clase/estáticos

class Estudiante(Persona):
    # Constructor: hereda nombre, edad, ciudad; añade nota_media
    def __init__(self, nombre, edad, ciudad="Desconocida", nota_media=0):
        super().__init__(nombre, edad, ciudad)  # Llama al constructor de Persona
        self.nota_media = nota_media            # Guarda la nota media

    def aprobo(self):
        # Devuelve True si la nota media es 5 o superior
        return self.nota_media >= 5

    # Método de clase: crea estudiante desde un string tipo "Nombre,Edad,Ciudad,Nota"
    @classmethod
    def crear_desde_string(cls, texto):
        partes = texto.split(",")
        nombre = partes[0]
        edad = int(partes[1])
        ciudad = partes[2]
        nota_media = float(partes[3])
        return cls(nombre, edad, ciudad, nota_media)

    # Método estático: verifica si una nota es válida (0 a 10)
    @staticmethod
    def es_valida_nota(nota):
        return 0 <= nota <= 10

    # Muestra información del estudiante, incluyendo si aprobó
    def __str__(self):
        estado = "Aprobado" if self.aprobo() else "Suspenso"
        return f"{self.nombre} ({self.edad} años, {self.ciudad}) - Nota: {self.nota_media} - {estado}"

# EJERCICIO 10: Composición (Coche tiene una Persona como propietario)

class Coche:
    # El propietario debe ser un objeto Persona
    def __init__(self, marca, modelo, propietario):
        self.marca = marca                # Marca del coche (str)
        self.modelo = modelo              # Modelo del coche (str)
        self.propietario = propietario    # Objeto Persona

    def __str__(self):
        # Muestra la información del coche y el nombre del propietario
        return f"{self.marca} {self.modelo} propiedad de {self.propietario.nombre}"

# -------------------------
# Ejemplos de uso/pruebas
# -------------------------

if __name__ == "__main__":
    # PRUEBA 1: Crear personas y usar métodos básicos
    print("--- Ejemplo Persona ---")
    persona1 = Persona("Ana", 25, "Madrid")       # Se crea una persona con ciudad
    persona2 = Persona("Luis", 30)                # Se crea una persona con ciudad por defecto
    persona1.presentarse()                        # Muestra presentación
    persona2.presentarse()
    persona1.cumplir_anios()                      # Incrementa la edad

    # PRUEBA 2: Ver el contador de instancias
    print(f"Total de personas creadas: {Persona.contador_personas}")

    # PRUEBA 3: Comprobar el setter de edad (propiedad)
    try:
        persona1.edad = -5                        # Intenta poner edad negativa
    except ValueError as e:
        print("Error:", e)

    # PRUEBA 4: Grupo con varias personas
    print("\n--- Ejemplo Grupo ---")
    grupo = Grupo()                               # Crea grupo vacío
    grupo.agregar_persona(persona1)               # Añade personas al grupo
    grupo.agregar_persona(persona2)
    grupo.mostrar_personas()                      # Muestra todas

    # PRUEBA 5: Estudiante con herencia, métodos de clase/estáticos
    print("\n--- Ejemplo Estudiante ---")
    estudiante1 = Estudiante("Marta", 20, "Valencia", 8.2)    # Crea estudiante normal
    print(estudiante1)
    print("¿Aprobó?", estudiante1.aprobo())                   # Verifica si aprobó

    # Crear estudiante desde un string
    estudiante2 = Estudiante.crear_desde_string("Ismael,23,Madrid,4.7")
    print(estudiante2)
    print("¿Nota válida 11?", Estudiante.es_valida_nota(11))  # Verifica validez nota

    # PRUEBA 6: Composición con Coche y Persona
    print("\n--- Ejemplo Coche ---")
    coche1 = Coche("Renault", "Clio", persona1)               # Crea coche con propietario
    print(coche1)

    # PRUEBA 7: Todos los objetos siguen funcionando
    print("\n--- Resumen Final ---")
    grupo.agregar_persona(estudiante1)        # Puedes agregar estudiantes a grupos de personas
    grupo.mostrar_personas()
