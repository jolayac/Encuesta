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
<<<<<<< Updated upstream
    def __init__(self, nombre, edad, respuesta_proyecto=None):
        self.nombre = nombre.capitalize()
        self.edad = edad
=======
    def __init__(self, nombre: str, edad: int, respuesta_proyecto=None):
        if respuesta_proyecto is None:
            respuesta_proyecto = {}
        self.nombre = nombre.strip().title()
        self.edad = int(edad)
>>>>>>> Stashed changes
        self.respuesta_proyecto = respuesta_proyecto

    @staticmethod
    def crear_estudiante_input():
<<<<<<< Updated upstream
        """Crea un nuevo estudiante (objeto). Pide un nombre y una edad en la terminal"""

        nombr = input("Ingrese su nombre.\n>").strip().title()

        while True:    # Se va a encargar de verificar que el input de edad sea válido como edad.
            try:
                eda = int(input("Ingrese su edad.\n>"))
                if 0 < eda < 120:
                    break
                else:
                    print("Por favor, ingrese una edad válida.")
            except ValueError:
                print("La edad debe ser un número entero coherente. Intente de nuevo")
        lista_estudiantes.append(nombr)

=======
        nombr = input("Ingrese su nombre.\n>")
        while True:
            eda_str = input("Ingrese su edad (número entero):\n> ").strip()
            try:
                eda = int(eda_str)
                break
            except ValueError:
                print("La edad debe ser un número entero. Intente de nuevo.")
>>>>>>> Stashed changes
        return Estudiante(nombr, eda)


class Encuesta:
    def __init__(self, estudiante):

        self. estudiante = estudiante
        self.preguntas = [
            "¿Está usted interesado en hacer un proyecto con ayuda de Python? (Sí/No)",
            "¿Cuál es su idea de proyecto?",
            "¿Tiene alguna experiencia programando con Python, Java o algún otro lenguaje de programación?\nDe ser así, indique cuál. De lo contrario, escriba \"No\"."
        ]
        self.respuestas = {
            "Interés": "",
            "Idea": "",
            "Experiencia": ""
        }

    def agregar_respuesta(self, estudiante):
        """
        Hace la encuesta: pregunta por el interés, idea de proyecto y experiencia programando.
        Después, guarda los resultados en la encuesta creada (objeto) y la guarda dentro del estudiante (respuesta_proyecto)
        El return es un extra, por si llega a ser necesario.
        """
        # Para interés. Solo acepta si o no en sus diferentes formas.
        while True:
            interes = input(self.preguntas[0] + "\n> ").strip().lower()
            if interes == "si":
                interes = "Sí"
            elif interes == "sí":
                interes = "Sí"
            elif interes == "no":
                interes = "No"
            else:
                print("Respuesta inválida. Por favor, responda \"Sí\" o \"No\".\n> ")

            if interes == "Sí":
                self.interesado = True
                break
            if interes == "No":
                self.interesado = False
                break

        # Para idea.
        idea = input(self.preguntas[1] + "\n>").strip().capitalize()

        # Para experiencia.
        experiencia = input(self.preguntas[2] + "\n>").strip().capitalize()

        # Para agregarlo a respuestas.
        self.respuestas["Interés"] = interes
        self.respuestas["Idea"] = idea
        self.respuestas["Experiencia"] = experiencia

        # Para incluirlo en estudiante.
        estudiante.respuesta_proyecto = self.respuestas
        lista_encuestas.append(self.respuestas)

        return self.respuestas

    def resumen(self, estudiante):
        """Crea un mensaje con las respuestas organizadas"""
        1 = "-" * 30
        2 = f"\nMuchas gracias por llenar el formulario, {estudiante.nombre}.\nResumen:"
        3 = "\n".join(for llave, valor in self.respuestas.items():
                      f" | {llave}: {valor}"


    @ staticmethod
    def mostrar_todos_los_resultados():
        for i in range(len(lista_estudiantes)):
            print(lista_estudiantes[i], lista_encuestas[i])



# Programa principal

def main():
    for i in range(1, 4):
        sujeto=Estudiante.crear_estudiante_input()
        encuesta1=Encuesta(sujeto)
        encuesta1.agregar_respuesta(sujeto)
        print(Encuesta.resumen(encuesta1, sujeto))
    Emcuesta.


main()
