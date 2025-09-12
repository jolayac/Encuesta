# Juan Sebastián Olaya Castañeda
# Juan Sebastián Corredor Saenz
# Juan Camilo Páez Guaspud

# Diseñar una encuesta para 6 users
# Nombre
# Interés en hacer un proyecto
# Idea de proyecto
# Experiencia con lenguajes

# clases

class Estudiante:
    def __init__(self, nombre, edad, respuesta_proyecto):
        self.nombre = nombre
        self.edad = edad
        self.respuesta_proyecto = mostrar_resultados()
        
class Encuesta:
    def __init__(self, preguntas, respuestas):
        self.preguntas = ["¿Está usted interesado en hacer un proyecto con ayuda de Python?", "¿Cuál es su idea de proyecto?","¿Tiene alguna experiencia programando con Python, Java o algún otro lenguaje de programación? De ser así, indique cuál"]
        self.respuestas = {"Interés": interes, "Idea": idea, "Experiencia": experiencia}

    def agregar_respuesta():
        interes = input(self.pregunta[0] + " ")
        idea = input(self.preguntas[1] + " ")
        experiencia = input(self.preguntas[2] + " ")

    def mostrar_resultados():
        pass

    def resumen():
        pass


# Variables:
Resultado = []
Resultados = []


User1 = {""}
User2 = {""}
User3 = {""}
User4 = {""}
User5 = {""}
User6 = {""}

# Funciones


def encuesta():
    Nombre = input("Ingrese su nombre: ")
    Carrera = input("Ingrese su carrera: ")
    Idea = input("Ingrese su idea de proyecto: ")
    return {"Nombre": Nombre, "Carrera": Carrera, "Idea": Idea}


# Programa principal
def main():
    for i in range(11):
        if i <= 5:
            Resultado = encuesta()
            Resultados.append(Resultado)
            print(f"User {i+1} {Resultado}")
            if i == 0:
                User1 = Resultado
            elif i == 1:
                User2 = Resultado
            elif i == 2:
                User3 = Resultado
            elif i == 3:
                User4 = Resultado
            elif i == 4:
                User5 = Resultado
            elif i == 5:
                User6 = Resultado
        elif i == 6:
            print("Gracias por participar en la encuesta")
            print("Los resultados son:")
            # Crea listas [i,resultado] más o menos así: [(1, 'A'), (2, 'B'), (3, 'C')]. (A, B y C siendo resultados).
            for i, resultado in enumerate(Resultados, 1):
                print(f"Usuario {i}:")
                print(f"  Nombre: {resultado['Nombre']}")
                print(f"  Carrera: {resultado['Carrera']}")
                print(f"  Idea de proyecto: {resultado['Idea']}")
                print("-" * 30)
        else:
            break
