# RÍOS PÉRES FANY

'''
Pasar de fecha a número:
Queremos dada una fecha asignarle un valor numérico
(el valor numérico será la cantidad de días que han pasado desde el año 0 hasta esa fecha)
para ello la fecha se separa en tres: día, mes y año
si es 02/03/1998 por ejemplo
la suma es:

Años:
vemos la cantidad de dias desde el 1 de enero del año 0 hasta 31 de diciembre 1997
es decir, contamos años completos (1997 años completos)
solamente teniendo cuidado en si cada año es bisiesto o no

Meses:
la cantidad de meses desde el 1 de enero de 1998 hasta el dia previo al 1 de marzo de 1998
es decir, contamos meses enteos (marzo-1 = 3-1 = 2 meses completos)
teniendo en cuenta en que si cada uno de esos meses contados es de 31 dias o  es febrero (entonces otro if para ver si es bisiesto
 y le asignamos 29 o 28 dias segun corresponda), o si es de 30 dias. 

Dias:
por ultimo los dias que ya nos las da la fecha original (2 dias en este caso)

sumamos esas tres cantidades y tenemos en número buscado:) suerte
'''

F1 = " 02/03/1998"
x = F1.split("/")
x = [int(x[0]), int(x[1]), int(x[2])]

def DiasDelMes (fecha:list):                #aqui el argumento es la fecha original ya una vez hecho el split
    ContadorMes = 0                         #vamos a contar los dias de 1 de enero al mes anterior al en curso
    for mes in range(1, fecha[1]):          #iteramos por cada numero de mes

        if fecha[2] % 4 == 0:               #aqui entonces deben tener en cuenta si es febrero: si es bisiesto
    
            if fecha[1] == 2:
                ContadorMes += 31           #también ver si tu mes tiene 30 o 31 dias, tengan en cuenta que los enero, marzo,mayo,julio,agosto,octubre,diciembre tienen 31
            elif fecha[1] == 3:
                ContadorMes += 31 + 29
            elif fecha[1] == 4: 
                ContadorMes += 31*(2) + 29
            elif fecha[1] == 5:
                ContadorMes += 31*(2) + 30*(1) + 29
            elif fecha[1] == 6:
                ContadorMes += 31*(3) + 30*(1) + 29
            elif fecha[1] == 7:
                ContadorMes += 31*(3) + 30*(2) + 29   
            elif fecha[1] == 8:
                ContadorMes += 31*(4) + 30*(2) + 29  
            elif fecha[1] == 9:
                ContadorMes += 31*(5) + 30*(2) + 29  
            elif fecha[1] == 10:
                ContadorMes += 31*(5) + 30*(3) + 29  
            elif fecha[1] == 11:
                ContadorMes += 31*(6) + 30*(3) + 29  
            elif fecha[1] == 12:
                ContadorMes += 31*(6) + 30*(4) + 29 
              
        else:
        
            if fecha[1] == 2:
                ContadorMes += 31
            elif fecha[1] == 3:
                ContadorMes += 31 + 28
            elif fecha[1] == 4: 
                ContadorMes += 31*(2) + 28
            elif fecha[1] == 5:
                ContadorMes += 31*(2) + 30*(1) + 28
            elif fecha[1] == 6:
                ContadorMes += 31*(3) + 30*(1) + 28
            elif fecha[1] == 7:
                ContadorMes += 31*(3) + 30*(2) + 28   
            elif fecha[1] == 8:
                ContadorMes += 31*(4) + 30*(2) + 28  
            elif fecha[1] == 9:
                ContadorMes += 31*(5) + 30*(2) + 28  
            elif fecha[1] == 10:
                ContadorMes += 31*(5) + 30*(3) + 28 
            elif fecha[1] == 11:
                ContadorMes += 31*(6) + 30*(3) + 28  
            elif mes == 12:
                ContadorMes += 31*(6) + 30*(4) + 28

        return ContadorMes

# print(DiasDelMes(x))


def DiasdelosAñosAnteriores (fecha):
    ContadorAños = 0
    for año in range(1,fecha[2]):           #iteramos por cada año del 0 al anterior del actual
        if año % 4 == 0:                    #entonces es bisiesto
            ContadorAños += 366
        else:
            ContadorAños += 365
    return(ContadorAños)

print(DiasdelosAñosAnteriores(x))

Numero = x[0] + DiasdelosAñosAnteriores(x) + DiasDelMes(x)
print(Numero)

