# Encuesta de idea de proyecto
Este programa permite recopilar información necesaria para nuestra clase a 6 usuarios a través de una encuesta interactiva. Cada usuario debe ingresar su nombre, carrera y una idea de proyecto final. Al final, se mostrarán estos datos de forma organizada.
# Autores
Juan Sebastián Olaya Castañeda,
Juan Sebastián Corredor Saenz,
Juan Camilo Páez Guaspud.
Descripción del Código

# El programa se compone de las siguientes variables:
Resultado = []
Resultados = []

User1 = {""}
User2 = {""}
User3 = {""}
User4 = {""}
User5 = {""}
User6 = {""}
# Su función principal :
def encuesta():
    Nombre = input("Ingrese su nombre: ")
    Carrera = input("Ingrese su carrera: ")
    Idea = input("Ingrese su idea de proyecto: ")
    return {"Nombre": Nombre, "Carrera": Carrera, "Idea": Idea}
# Lógica del programa :
-El programa ejecuta un ciclo usando for para realizar la encuesta a 6 usuarios.
-Cada respuesta se guarda en una lista llamada Resultados.
-Al finalizar, se imprime un resumen con los datos de cada participante.
# Ejecución y salida :
Para ejecutar el programa, simplemente corre el script en Visual Studio Code, E ingresa los datos de cada usuario uno por uno.
<img width="523" height="124" alt="image" src="https://github.com/user-attachments/assets/e9f22e21-3f1e-4250-9317-3a8c4f1d27bf" />
