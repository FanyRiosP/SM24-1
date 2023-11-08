# RÍOS PÉREZ FANY

#F1=" 02/03/1998"
F1="6/11/1492"


def DiasDelMes(fecha):                 # aqui la fecha original ya una vez hecho el split
    ContadorMes = 0                    # vamos a contar los dias de 1 de enero al mes en curso
    for mes in range(1, fecha[1]):     # iteramos por cada numero de mes
        if mes <= 7:                   # de enero a julio
            if mes % 2 != 0:           # si es impar, son 31 dias
                ContadorMes += 31

            else:                           # si fue par
                if mes == 2:                # vemos si es febrero
                    if fecha[2] % 4 == 0:   # entonces es bisiesto y febrero
                        ContadorMes += 29
                    else:
                        ContadorMes += 28
                else:                       # no fue febrero y fue par
                    ContadorMes += 30
        else:                               # de agosto a diciembre, porque julio es impar y agosto es par pero ambos tienen 31 dias
            if mes % 2 != 0:                # si es impar, son 30 dias
                ContadorMes += 30
            else:                           # si fue par, ya no tenemos que ver si es febrero porque estamos del mes 8 en adelante, y agosto, cotubre y diciembre tienen 31
                ContadorMes += 31
    return ContadorMes


def DiasdelosAñosAnteriores(fecha):
    ContadorAños = 0
    for año in range(1, fecha[2]):      # iteramos por cada año del 0 al anterior del actual
        if año % 4 == 0:                # entonces es bisiesto
            ContadorAños += 366
        else:
            ContadorAños += 365
    return (ContadorAños)


def Numero_de_fecha(F1):                #metemos todo en una funcion que dada una fecha en string me da un numero
    x=F1.split("/")
    x=[int(i) for i in x]               #pasamos los valores del split que son cadenas a enteros para poder operar
    Numero = x[0] + DiasdelosAñosAnteriores(x) + DiasDelMes(x)
    return Numero
#print(Numero_de_fecha(F1)) #vemos que funciona


#----------------------------------------------------------------------------------------------------------------------

'''
Ahora el ejercicio es
dadas dos fechas F1,F2. Y suponiendo que hay un evento que ocurrió en esas dos fechas y se repite de forma periódica
por determinar la fecha final o F3 en la que ese evento se va a repetir después del presente
definamos F1,F2 y la fecha actual como FA
'''

F1="20/04/1909"     #son fechas del cometa halley :)
F2="9/02/1982"
FA="01/09/2023"

#obtenemos sus numeros respectivos
N1 = Numero_de_fecha(F1)
N2 = Numero_de_fecha(F2)
NA = Numero_de_fecha(FA)

#obtenemos la distancia entre F1 y F2 para saber cada cuando pasa el evento
distancia = N2 - N1

#vemos cuantas veces podemos sumarle esa distancia a N1 antes de rebasar la fecha actual (NA)
Contadorveces = 0
while True:
    if N1 + ((Contadorveces+1)*distancia) > NA:
        break;          # si ya rebasamos NA, lo que metí en contador de veces ya es el número que busco
    else:               # aun no lo rebasa, entonces puedo agregarlo una vez más
        Contadorveces += 1

#cuando sale del while ya tenemos el Contadorveces que buscamos
#guardamos ese valor en una variable, como ese valor es sumando contadorveces el lapso del tiempo en el cual se repite
#ese valor corresponde a la ultima vez que sucedio el evento
ultimaVez = N1 + ((Contadorveces)*distancia)

#para la fecha final, primero restamos el tiempo que ya pasó, es decir, la fecha actual - ultima vez
TiempoTranscurrido= NA - ultimaVez

#si a la distancia le quitamos el tiempo trasncurrido, nos quedan los dias que faltan para el siguiente evento!!
DiasQueFaltan = distancia - TiempoTranscurrido
print(distancia)
print("faltan ", str(DiasQueFaltan), " Días :)")
#de estos dos datos vamos que vamos más o menos a la mitad de camino para el siguiente paso del cometa halley
#ahora sólo falta volver a convertir el numero respectivo a la fecha del siguiente evento (FA+DiasQueFaltan) convertirlo a una fecha


#----------------------------------------------------------------------------------------------------------------------

'''
Sea "Numero_de_fecha()" la función que crearon en el Ejercicio 3 que a una fecha le asigna un valor numérico
Ahora, dada una Fo (Fecha inicial o dada), dada una M (numero entero positivo),
ustedes conocen la fecha actual y dia de la semana actual. 

Lo que harán es, con esa información obtener:

1- Qué número le corresponde a la Fecha2 o F2 = Numero_de_fecha(Fo) + M
pueden usar de ejemplo a Fo = "07/11/1990" y M=200
2- Ese número asociado a la fecha 2, ahora hagan la función inversa y diganme que fecha (dia/mes/año) es el numero obtenido en el punto 1. 
En otras palabras: que fecha es la Fecha2
3-Sabiendo la fecha de hoy y el dia de la semana de hoy, qué día de la semana corresponde a la Fecha2? (lunes, martes, miercoles...)
  
Hint: a) obtengan k tal que 7*k + Fecha2 = Fecha actual (despejen) 
      b) quedense con los decimales de k, dividanlo entre 100 y obtienen una fraccion p/q
      c) multiplican esa fraccion p/q por q/7 y el resultado (R) es la cantidad de dias de la semana (del 1 al 7) anteriores a la fecha                            actual. Por ejemplo, si R es 4 y ustedes definieron al viernes como 7, 7-4 es 3 entonces jueves le corresponde el 6, miercoles 5, martes 4, lunes 3, entonces la Fecha2 fue un lunes. 
'''

