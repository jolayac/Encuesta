Autor: Juan Sebastián Olaya Castañeda.

Este programa permite recopilar información necesaria para nuestra clase a 10 usuarios a través de una encuesta interactiva. Cada usuario debe ingresar su nombre, carrera y una idea de proyecto final. Al final, se mostrarán estos datos de forma organizada.

>Nota: Realmente me esforcé por hacer esoto lo mejor que pude. Consulté, proble, corregí, investigé y vi tutoriales para logar hacer lo que considero un buen proyecto. Aprendí más mientras hacía este archivo que en todo el curso de programación que tomé el semestre pasado.

# Input/Output
Un estudiante debe comenzar a llenar un formulario. Se crea su "perfil" como estudiante y después se le hacen unas preguntas relacionadas a lo que planea hacer como proyecto. Esto se repite 10 veces, con 10 estudiantes diferentes.

![alt text](<Screenshot 2025-09-16 at 00.30.39.png>)

Al final, se muestran todas las respuestas que los estudiantes hicieron.

![alt text](<Screenshot 2025-09-16 at 00.31.43.png>)

# Condiciones
Las respuestas no se pueden dejar vacías y algunas preguntas solo aceptan cierto tipo de datos:
-Edad (entero entre 5 y 100).
![alt text](<Screenshot 2025-09-16 at 01.00.14.png>)

![alt text](<Screenshot 2025-09-16 at 00.39.21.png>)


-Interés (Sí/No).
![alt text](<Screenshot 2025-09-16 at 01.00.14-1.png>)

![alt text](<Screenshot 2025-09-16 at 00.39.52.png>)

# Clases
Hay dos clases: Estudiante y Encuesta. Cada una tiene  diferentes variabes que se actualizan con los datos introducidos en la terminal, una funció que crea la instancia y diferentes funciones para hacer el formulario y guardar datos en variables

## Estudiante
### Datos
Clase que almacenan nombre, edad y los resultados de la encuesta. 
![alt text](<Screenshot 2025-09-16 at 00.47.10.png>)

### Funciones
Puede crear una instancia con la función `.crear_estudiante_input()`.
![alt text](<Screenshot 2025-09-16 at 01.12.25.png>)

## Encuesta
### Datos
Almacena las preguntas, las respuestas dadas por el estudiante y un mensaje con la respuestas organizadas.
![alt text](<Screenshot 2025-09-16 at 01.12.25-1.png>)

### Funciones
#### `.agregar_respuesta(estudiante)`
Con este comando se crea la instancia, se hacen las preguntas, se recibe el input con las repuestas y guarda las respuestas en esa misma instancia y la del estudiante.
>No le tomo captura porque quedaría muy extensa

#### `.respuesta_organizada()`
Crea un mensaje personalizado en el que se muestran las respuestas de manera ordenada. Se utiliza al final del programa, para mostrar todos los resutados de manera corta.
![alt text](<Screenshot 2025-09-16 at 01.28.42.png>)

![alt text](<Screenshot 2025-09-16 at 01.31.00.png>)

#### `.resumen(estudiante)`
Es como la anterior, con la diferencia de que esta vez se muestra un mensaje de agradecimiento al estudiante.
![alt text](<Screenshot 2025-09-16 at 01.35.13.png>)

>La función `mostrar_todos_los_resultados(lista1, lista2)` se encarga de imprimir alternadamente el nombre de cada estudiante y sus respuestas.

# Programa principal
Organiza las funciones para que:
1. Cree un nuevo estudiante pidiéndole sus datos desde la terminal.
2. Cree un objeto encuesta en base al estudiante anteriormente creado.
3. Imprima un mensaje que le muestre al estudiante un resumen de las respuestas que dio.
Esto lo hace 10 veces, creando 10 instancias de estudiantes y 10 de encuestas.
4. Separado, muestra todos los resultados de las encuestas en la terminal.

![alt text](<Screenshot 2025-09-16 at 01.36.37.png>)