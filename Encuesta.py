# Juan Sebastián Olaya Castañeda

"""
Diseñar una encuesta para 10 usuarios, que organice y muestre los resultados.
Datos que pide la encuesta:
-Interés en hacer un proyecto.
-Idea de proyecto.
-Experiencia programando.
"""
import unicodedata # Para normalizar cadenas.

class Estudiante:
    def __init__(self, nombre, edad, respuesta_proyecto=None):
        self.nombre = nombre.capitalize()
        self.edad = edad
        self.respuesta_proyecto = respuesta_proyecto
    @staticmethod
    def crear_estudiante_input():
        nombr = input("Ingrese su nombre.\n>")
        nombr = nombr.strip()
        nombr = nombr.capitalize()
        while True:
            try:
                eda = int(input("Ingrese su edad.\n>"))
                if eda <= 0:
                    print("Por favor, ingrese una edad válida.")
                    continue
                break
            except ValueError:
                print("La edad debe ser un número entero. Intente de nuevo")
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
        # Para interes.
        valido = True
        while valido:
            interes = unicodedata.normalize("NFD", str(input(self.preguntas[0] + "\n> "))) # Normaliza la cadena. En caso de que haya un "sí", pasa a "si".
            interes = interes.strip()
            interes = interes.lower()
            if interes == "si":
                interes = "Sí"
            elif interes == "no":
                interes = "No"
            if interes == "Sí" or interes == "No":
                valido = False
            else:
                print("Respuesta inválida. Por favor, responda \"Sí\" o \"No\".\n> ")
        # Para idea.
        idea = str(input(self.preguntas[1] + " "))
        idea = idea.strip()
        idea = idea.capitalize()
        # Para experiencia.
        experiencia = str(input(self.preguntas[2] + " "))
        experiencia = experiencia.strip()
        experiencia = experiencia.lower()
        if experiencia == "no":
            experiencia = "No"
        # Para agregarlo a respuestas.
        self.respuestas["Interés"] = interes
        self.respuestas["Idea"] = idea
        self.respuestas["Experiencia"] = experiencia
        # Para incluirlo en estudiante.
        estudiante.respuesta_proyecto = self.respuestas
        return self.respuestas

    def mostrar_resultados(self):
        for llave, valor in self.respuestas.items():
            print(f"{llave}: {valor}\n")

    def resumen(self):
        positivos = 0
        negativos = 0
        if self.respuestas["Interés"] == "Sí":
            positivos += 1
        elif self.respuestas["Interés"] == "No":
            negativos += 1
        total = positivos + negativos
        resumen = {
            "total": total,
            "Cantidad de Sí": positivos,
            "Cantidad de No": negativos
        }
        return resumen


lista_estudiantes = []
lista_encuestas = []

# Programa principal


def main():
    for i in range(1, 3):
        sujeto = Estudiante.crear_estudiante_input()
        lista_estudiantes.append(sujeto)
        encuesta1 = Encuesta(sujeto)
        encuesta1.agregar_respuesta(sujeto)
        lista_encuestas.append(encuesta1)
        encuesta1.mostrar_resultados()


main()
