'''
pedir al usuario la calificación de los dos parciales
'''
def calcular_promedio(cal1, cal2):
    return (cal1+cal2)/2
def apreba(cal):
    return cal >= 70

calificaion1 = float(input("Escribe la calificaion del parcial 1: "))
calificaion2 = float(input("Escribe la calificaion del parcial 2: "))

if calificaion1 >= 0 and calificaion1 <= 100 :
    if calificaion2 >= 0 and calificaion2 <= 100:
        #Promediar y verificar si aprobo
        promedio = calcular_promedio(calificaion1, calificaion2)
        if apreba (promedio) :
            print("Aprovaste el semestre")
        else :
            print("nos vemos el siguiente semestre")
    else:
        print("La calificacion del parcial 2 es incorrecta")
else : 
      print("La calificacion del parcial 1 es incorrecta")
 