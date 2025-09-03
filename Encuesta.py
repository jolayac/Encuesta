#Juan Sebastián Olaya Castañeda
#Juan Sebastián Corredor Saenz
#Juan Camilo Páez Guaspud

#Diseñar una encuesta para 6 users
#Nombre
#Carrera
#Idea de proyecto

#Variables:
Resultado=[]
Resultados=[]


User1={""}
User2={""}
User3={""}
User4={""}
User5={""}
User6={""}



def encuesta ():
    Nombre=input("Ingrese su nombre: ")
    Carrera=input("Ingrese su carrera: ")
    Idea=input("Ingrese su idea de proyecto: ")
    return {"Nombre":Nombre, "Carrera":Carrera, "Idea":Idea}

for i in range(7):
    if i <=5:
        Resultado=encuesta()
        Resultados.append(Resultado)
        print (f"User {i+1} {Resultado}")
        if i==0:
            User1=Resultado
        elif i==1:
            User2=Resultado
        elif i==2:
            User3=Resultado     
        elif i==3:
            User4=Resultado
        elif i==4:
            User5=Resultado
        elif i==5:
            User6=Resultado
    elif i==6:
        print("Gracias por participar en la encuesta")
        print("Los resultados son:")
        for i, resultado in enumerate(Resultados, 1):
            print(f"Usuario {i}:")
            print(f"  Nombre: {resultado['Nombre']}")
            print(f"  Carrera: {resultado['Carrera']}")
            print(f"  Idea de proyecto: {resultado['Idea']}")
            print("-" * 30)
