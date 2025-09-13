# Juan Sebastián Olaya Castañeda

"""
Diseñar una encuesta para 10 usuarios, que organice y muestre los resultados.
Datos que pide la encuesta:
-Interés en hacer un proyecto.
-Idea de proyecto.
-Experiencia programando.
"""

# clases
# x = {"as" : 1, "asdafs" : 2}
# print(list(x)[0][0])


class Estudiante:
    def __init__(self, nombre, edad, respuesta_proyecto):
        self.nombre = nombre
        self.edad = edad
        self.respuesta_proyecto = respuesta

    def crear_estudiante(self, nombre, edad):


class Encuesta:
    def __init__(self, estudiante):
        self.preguntas = [
            "¿Está usted interesado en hacer un proyecto con ayuda de Python? (Sí/No)",
            "¿Cuál es su idea de proyecto?",
            "¿Tiene alguna experiencia programando con Python, Java o algún otro lenguaje de programación?\nDe ser así, indique cuál. De lo contrario, escriba \"No\""
        ]
        self.respuestas = {
            "Interés": "",
            "Idea": "",
            "Experiencia": ""
        }

    def agregar_respuesta(self):
        # Para interes.
        valido = True
        while valido:
            interes = str(input(self.pregunta[0] + "\n>"))
            interes = interes.strip()
            interes = interes.lower()
            if "s" in interes:
                interes = "Sí"
            elif "n" in interes:
                interes = "No"
            if interes == "Sí" or interes == "No":
                valido = False
            else:
                print("Respuesta inválida. Por favor, responda \"Sí\" o \"No\".")
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
        # Idea: hacer un return con el diccionario si no funciona.

    def mostrar_resultados(self):
        pass

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
        return list(resumen)


# Programa principal
def main():
    nombre_estuiante = input("Ingrese su nombre.")
    edad_estudiante = input("Ingrese su edad.\n>")
    Estudiante1 = Estudiante(nombre_estuiante, edad_estudiante)


main()
