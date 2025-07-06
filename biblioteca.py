# -----------------------------------------------------------
# Ejercicio: Gestión de Biblioteca
# 
# 1. Clase Libro con título, autor, año y estado prestado.
#    Métodos para prestar, devolver y mostrar información.
# 2. Clase Biblioteca que gestiona una lista de libros,
#    permite agregarlos, mostrarlos, prestarlos y devolverlos.
# 3. Menú para gestionar todo desde el programa principal.
# -----------------------------------------------------------

class Libro:
    def __init__(self, titulo, autor, anio):
        # Constructor: Inicializa los atributos del libro
        self.titulo = titulo        # Título del libro (str)
        self.autor = autor          # Autor del libro (str)
        self.anio = anio            # Año de publicación (int)
        self.prestado = False       # Estado: prestado o no (bool, por defecto False)

    def prestar(self):
        # Método para prestar el libro
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        # Método para devolver el libro
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def __str__(self):
        # Muestra la información del libro y su estado
        estado = "Prestado" if self.prestado else "Disponible"
        return f"'{self.titulo}' de {self.autor} ({self.anio}) - {estado}"


class Biblioteca:
    def __init__(self):
        # Constructor: Inicializa la lista vacía de libros
        self.catalogo = []

    def agregar_libro(self, libro):
        # Añade un libro al catálogo
        self.catalogo.append(libro)
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def mostrar_libros(self):
        # Muestra tod2os los libros del catálogo
        if not self.catalogo:
            print("La biblioteca está vacía.")
        else:
            print("\nCatálogo de libros:")
            for libro in self.catalogo:
                print(" -", libro)

    def prestar_libro(self, titulo):
        # Busca un libro por título y lo presta si es posible
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                libro.prestar()
                return
        print(f"No se encontró ningún libro con el título '{titulo}'.")

    def devolver_libro(self, titulo):
        # Busca un libro por título y lo devuelve si es posible
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                libro.devolver()
                return
        print(f"No se encontró ningún libro con el título '{titulo}'.")


def menu():
    # Menú interactivo principal
    biblioteca = Biblioteca()  # Crea una biblioteca vacía
    while True:
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Añadir libro")
        print("2. Mostrar libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Añadir libro
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = input("Año: ")
            try:
                anio = int(anio)
                libro = Libro(titulo, autor, anio)
                biblioteca.agregar_libro(libro)
            except ValueError:
                print("El año debe ser un número entero.")
        elif opcion == "2":
            # Mostrar libros
            biblioteca.mostrar_libros()
        elif opcion == "3":
            # Prestar libro
            titulo = input("Título del libro a prestar: ")
            biblioteca.prestar_libro(titulo)
        elif opcion == "4":
            # Devolver libro
            titulo = input("Título del libro a devolver: ")
            biblioteca.devolver_libro(titulo)
        elif opcion == "5":
            # Salir del programa
            print("¡Hasta luego!")
            break
        else:
            # Opción no válida
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    # Ejecuta el menú solo si este archivo es el principal
    menu()
