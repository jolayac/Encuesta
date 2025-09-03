#Juan Sebastián Olaya Castañeda
#Juan Sebastián Corredor Saenz
#Juan Camilo Páez Guaspud

#Diseñar una encuesta para 6 users
#Nombre
#Carrera
#Idea de proyecto

#def encuesta ():
User1={"Nombre":"", "Carrera":"", "Idea":""}
User2={"Nombre":"", "Carrera":"", "Idea":""}
User3={"Nombre":"", "Carrera":"", "Idea":""}



def encuesta ():
    Nombre=input("Ingrese su nombre: ")
    Carrera=input("Ingrese su carrera: ")
    Idea=input("Ingrese su idea de proyecto: ")
    return {"Nombre":Nombre, "Carrera":Carrera, "Idea":Idea}

print(encuesta ())

