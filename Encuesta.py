# Juan Sebastián Olaya Castañeda

"""
Diseñar una encuesta para 10 usuarios, que organice y muestre los resultados.
Datos que pide la encuesta:
-Interés en hacer un proyecto.
-Idea de proyecto.
-Experiencia programando.
"""
# Variables:

lista_estudiantes = []
lista_encuestas = []


# Clases:

class Estudiante:
    def __init__(self, nombre, edad, respuesta_proyecto=None):
        self.nombre = nombre
        self.edad = edad
        self.respuesta_proyecto = respuesta_proyecto

    @staticmethod
    def crear_estudiante_input():
        """Crea un nuevo estudiante (objeto). Pide un nombre y una edad en la terminal"""
        while True:    # Se va a encargar de verificar que el input de nombre no esté vacío.
            nombre = input("\nIngrese su nombre.\n> ").strip().title()
            if nombre == "":
                print("\nEl nombre no puede estar vacío. Intente de nuevo.")
            else:
                break

        while True:    # Se va a encargar de verificar que el input de edad sea un entero coherente.
            try:
                edad = int(input("\nIngrese su edad.\n> "))
                if 5 <= edad < 100:
                    break
                else:
                    print("\nPor favor, ingrese una edad válida.")
            except ValueError:
                print("\nLa edad debe ser un número entero coherente. Intente de nuevo")
        lista_estudiantes.append(nombre)

        return Estudiante(nombre, edad)


class Encuesta:
    def __init__(self):

        self.preguntas = [
            "¿Está usted genuinamente interesado en hacer un proyecto con ayuda de Python? (Sí/No)",
            "¿Cuál es su idea de proyecto?",
            "¿Tiene alguna experiencia programando con Python, Java o algún otro lenguaje de programación?\nDe ser así, indique cuál. De lo contrario, escriba \"No\"."
        ]
        self.respuestas = {
            "Interés": "",
            "Idea": "",
            "Experiencia": ""
        }
        self.resumen_respuestas = None

    def agregar_respuesta(self, estudiante):
        """
        Hace la encuesta: pregunta por el interés, idea de proyecto y experiencia programando.
        Después, guarda los resultados en la encuesta creada (objeto) y la guarda dentro del estudiante (respuesta_proyecto)
        El return es un extra, por si llega a ser necesario.
        """
        # Para interés. Solo acepta si o no en sus diferentes formas.
        print("\n")
        while True:
            interes = input(f"{self.preguntas[0]}\n> ").strip().lower()
            if interes == "si":
                interes = "Sí"
            elif interes == "sí":
                interes = "Sí"
            elif interes == "no":
                interes = "No"
            else:
                print("\nRespuesta inválida. Por favor, responda \"Sí\" o \"No\".\n")

            if interes == "Sí":
                self.interesado = True
                break
            if interes == "No":
                self.interesado = False
                break

        # Para idea.
        while True:
            idea = input(f"\n{self.preguntas[1]}\n> ").strip().capitalize()
            if idea == "":
                print("Mensaje vacío. Debe ingresar una respuesta.")
            else:
                break

        # Para experiencia.
        while True:
            experiencia = input(
                f"\n{self.preguntas[2]}\n> ").strip().capitalize()
            if experiencia == "":
                print("Mensaje vacío. Debe ingresar una respuesta.")
            else:
                break

        # Para agregarlo a respuestas.
        self.respuestas["Interés"] = interes
        self.respuestas["Idea"] = idea
        self.respuestas["Experiencia"] = experiencia

        # Para incluirlo en estudiante.
        estudiante.respuesta_proyecto = self.respuestas
        mensaje_completo = self.resumen(estudiante)
        self.resumen_respuestas = mensaje_completo
        lista_encuestas.append(self.respuesta_organizada())

    def respuesta_organizada(self):
        """Crea un mensaje con las respuestas organizadas"""
        separador = "-" * 30
        respuestas_lista = []
        for llave, valor in self.respuestas.items():
            respuestas_lista.append(f" | {llave}: {valor}")
        respuestas = "\n".join(respuestas_lista)
        mensaje_completo = f"{separador}\n{respuestas}\n{separador}"

        return mensaje_completo

    def resumen(self, estudiante):
        """Crea un mensaje con las respuestas organizadas"""
        separador = "-" * 30
        agradecimiento = f"Muchas gracias por llenar el formulario, {estudiante.nombre}.\n\nResumen:"
        respuestas_lista = []
        for llave, valor in self.respuestas.items():
            respuestas_lista.append(f" | {llave}: {valor}")
        respuestas = "\n".join(respuestas_lista)
        mensaje_completo = f"\n{separador}\n{agradecimiento}\n{respuestas}\n{separador}"

        return mensaje_completo


def mostrar_todos_los_resultados(lista1, lista2):
    print("Todos los resultados de las encuestas son los siguientes:")
    for i in range(len(lista1)):
        print(f"\n{lista1[i]}\n{lista2[i]}")

# Programa principal


def main():
    for i in range(1, 11):
        sujeto = Estudiante.crear_estudiante_input()
        encuesta = Encuesta()
        encuesta.agregar_respuesta(sujeto)
        print(encuesta.resumen_respuestas)
    print(f"\n{"=" * 30}\n")
    mostrar_todos_los_resultados(lista_estudiantes, lista_encuestas)


main()
