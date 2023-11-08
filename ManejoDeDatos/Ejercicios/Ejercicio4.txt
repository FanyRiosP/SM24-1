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


#print(Numero_de_fecha(FA))

fechaNueva = []

def Dias_a_fecha (fecha, dias):
    #fechaNueva = []
    fechaEnNumero = Numero_de_fecha(fecha)
    numeroNuevo = fechaEnNumero + dias

    # en un siglo hay 25 años bisiestos (1/4) c:
    diasDeAñosBisiestos = numeroNuevo // 4
    diasDeAñosNormales = numeroNuevo - diasDeAñosBisiestos

    # Ahora, obtenemos los años bisiestos y normales con la parte entera de dividir los diasDeAños... entre 366 y 365 respectivamente 
    # Con el residuo de dichas divisiones botenemos los día que no completan un año
    totalDeAños = (diasDeAñosBisiestos // 366) + (diasDeAñosNormales // 365)
    diasAConvertir = (diasDeAñosBisiestos % 366) + (diasDeAñosNormales % 365)

    # Si el totalDeAños es bisiesto, los diasAConvertir tendrían un día más para comparar
    if totalDeAños % 4 == 0:
        if diasAConvertir <= 31:
            dias = diasAConvertir
            fechaNueva.extend([dias, 1])
        elif diasAConvertir > 31 and diasAConvertir <= 60:
            dias = diasAConvertir - 31
            fechaNueva.extend([dias, 2])
        elif diasAConvertir > 60 and diasAConvertir <= 91:
            dias = diasAConvertir - 60
            fechaNueva.extend([dias, 3])
        elif diasAConvertir > 91 and diasAConvertir <= 121:
            dias = diasAConvertir - 91
            fechaNueva.extend([dias, 4])
        elif diasAConvertir > 121 and diasAConvertir <= 152:
            dias = diasAConvertir - 121
            fechaNueva.extend([dias, 5])
        elif diasAConvertir > 152 and diasAConvertir <= 182:
            dias = diasAConvertir - 152
            fechaNueva.extend([dias, 6])
        elif diasAConvertir > 182 and diasAConvertir <= 213:
            dias = diasAConvertir - 182
            fechaNueva.extend([dias, 7])
        elif diasAConvertir > 213 and diasAConvertir <= 244:
            dias = diasAConvertir - 213
            fechaNueva.extend([dias, 8])
        elif diasAConvertir > 244 and diasAConvertir <= 274:
            dias = diasAConvertir - 244
            fechaNueva.extend([dias, 9])
        elif diasAConvertir > 274 and diasAConvertir <= 305:
            dias = diasAConvertir - 274
            fechaNueva.extend([dias, 10])
        elif diasAConvertir > 305 and diasAConvertir <= 335:
            dias = diasAConvertir - 305
            fechaNueva.extend([dias, 11])
        elif diasAConvertir > 335 and diasAConvertir < 366:
            dias = diasAConvertir - 335
            fechaNueva.extend([dias, 12])
    else:
        if diasAConvertir <= 31:
            dias = diasAConvertir
            fechaNueva.extend([dias, 1])
        elif diasAConvertir > 31 and diasAConvertir <= 59:
            dias = diasAConvertir - 31
            fechaNueva.extend([dias, 2])
        elif diasAConvertir > 59 and diasAConvertir <= 90:
            dias = diasAConvertir - 59
            fechaNueva.extend([dias, 3])
        elif diasAConvertir > 90 and diasAConvertir <= 120:
            dias = diasAConvertir - 90
            fechaNueva.extend([dias, 4])
        elif diasAConvertir > 120 and diasAConvertir <= 151:
            dias = diasAConvertir - 120
            fechaNueva.extend([dias, 5])
        elif diasAConvertir > 151 and diasAConvertir <= 181:
            dias = diasAConvertir - 151
            fechaNueva.extend([dias, 6])
        elif diasAConvertir > 181 and diasAConvertir <= 212:
            dias = diasAConvertir - 181
            fechaNueva.extend([dias, 7])
        elif diasAConvertir > 212 and diasAConvertir <= 243:
            dias = diasAConvertir - 212
            fechaNueva.extend([dias, 8])
        elif diasAConvertir > 243 and diasAConvertir <= 273:
            dias = diasAConvertir - 243
            fechaNueva.extend([dias, 9])
        elif diasAConvertir > 273 and diasAConvertir <= 304:
            dias = diasAConvertir - 273
            fechaNueva.extend([dias, 10])
        elif diasAConvertir > 304 and diasAConvertir <= 334:
            dias = diasAConvertir - 304
            fechaNueva.extend([dias, 11])
        elif diasAConvertir > 334 and diasAConvertir < 365:
            dias = diasAConvertir - 334
            fechaNueva.extend([dias, 12])

    fechaNueva.append(totalDeAños)


Dias_a_fecha(FA, DiasQueFaltan)
print(fechaNueva)