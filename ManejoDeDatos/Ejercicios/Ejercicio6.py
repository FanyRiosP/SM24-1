import numpy as np
import random
import pygame


CalInicial=[[1, 'domingo'], [2, 'lunes'], [3, 'martes'], [4, 'miercoles'], [5, 'jueves'], [6, 'viernes'], [7, 'sabado'], [8, 'domingo'], [9, 'lunes'], [10, 'martes'], [11, 'miercoles'], [12, 'jueves'], [13, 'viernes'], [14, 'sabado'], [15, 'domingo'], [16, 'lunes'], [17, 'martes'], [18, 'miercoles'], [19, 'jueves'], [20, 'viernes'], [21, 'sabado'], [22, 'domingo'], [23, 'lunes'], [24, 'martes'], [25, 'miercoles'], [26, 'jueves'], [27, 'viernes'], [28, 'sabado'], [29, 'domingo'], [30, 'lunes'], [31, 'martes']]

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
#ancho = int(input("ingrese el ancho del tablero: "))
ancho=50
ventana_ancho = 600
ventana_alto = 600
pygame.init()
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Calendario")


cantidadRectasV=7
cantidadRectasH=7

Distancia_entre_rectasV = ventana_ancho // cantidadRectasV
Distancia_entre_rectasH = ventana_alto // cantidadRectasH


inicio = 0


ListaCoordenadasRectasV=[]
ListaCoordenadasRectasH=[]

#las rectas no van a cambiar entonces las declaramos aqui
for i in range(1,cantidadRectasV): #y hacemos las coordenadas para las rectas
    #cada recta requiere dos coordenadas, las iniciales y las finales, entonces, hacemos una lista de dos entradas para cada coordenada [ xi, yi ]
    #y luego una lista para ambas coordenadas de una recta [[x1.y1],[x2,y2]]
    #y finalmente esa lista la metemos en mi listacoordenadasrectas
    auxiliar=[]
    coordIniciales=[Distancia_entre_rectasV*(i),0]
    coordFInales=[Distancia_entre_rectasV*(i),ventana_ancho]
    auxiliar.append(coordIniciales)
    auxiliar.append(coordFInales)

    ListaCoordenadasRectasV.append(auxiliar)


#lo mismo para las horizontales
for i in range(1, cantidadRectasH):
    auxiliar = []
    coordIniciales = [0, Distancia_entre_rectasH * (i)]
    coordFInales = [ventana_alto, Distancia_entre_rectasH * (i)]
    auxiliar.append(coordIniciales)
    auxiliar.append(coordFInales)
    ListaCoordenadasRectasH.append(auxiliar)

print(ListaCoordenadasRectasV)
print(ListaCoordenadasRectasH)
Run = True
#para las letras sera
# primero los parametros son fuente,tamaño de letra
font = pygame.font.Font('freesansbold.ttf', 15)

while Run:
    pygame.time.delay(100)  # es en milisegundos
    for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si le das al tache de la pantalla, finaliza el programa
                Run = False

            #por ahora no haremos ninguna operacion más que imprimir las rectas y labels



    ventana.fill((0, 0, 0))
    for recta in ListaCoordenadasRectasH: #ahi la variable recta es mi lista [[x1.y1],[x2,y2]]
        pygame.draw.line(ventana, (0, 255, 255), (recta[0][0], recta[0][1]), (recta[1][0], recta[1][1]))
    for recta in ListaCoordenadasRectasV:  # ahi la variable recta es mi lista [[x1.y1],[x2,y2]]
        pygame.draw.line(ventana, (0, 255, 255), (recta[0][0], recta[0][1]), (recta[1][0], recta[1][1]))
    contadorH=0
    ya_anotamos_dia1=0
    for semario in ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]:
        # los parametros del texto son el texto, un "antialias" (siempre ponganle true), luego el color de letra y el color del fondo del rectangulo donde van als letras
        text = font.render(semario, True, green, (0, 0, 0))
        # creas el rectangulo donde pondremos las letras
        textRect = text.get_rect()
        # las coordenadas son el centro del rectangulo donde se ponen las letras
        textRect.center = (40+(contadorH*Distancia_entre_rectasV), 50)
        ventana.blit(text, textRect)
        contadorH+=1
        #una vez vamos en un dia, pondremos el numero de ese dia
        contadorV=1

        for dia in CalInicial:

            if dia[1] == semario and dia[0]==1:
                text = font.render(str(dia[0]), True, green, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (40 + ((contadorH - 1) * Distancia_entre_rectasV), 50 + (contadorV * Distancia_entre_rectasH))
                ventana.blit(text, textRect)

                ya_anotamos_dia1=1
                contadorV += 1
            elif dia[1]==semario and ya_anotamos_dia1==0:
                contadorV += 1
                text = font.render(str(dia[0]), True, green, (0,0,0))
                textRect = text.get_rect()
                textRect.center = (40+((contadorH-1)*Distancia_entre_rectasV), 50+(contadorV*Distancia_entre_rectasH))
                ventana.blit(text, textRect)

            elif dia[1]==semario and ya_anotamos_dia1==1:

                text = font.render(str(dia[0]), True, green, (0,0,0))
                textRect = text.get_rect()
                textRect.center = (40+((contadorH-1)*Distancia_entre_rectasV), 50+(contadorV*Distancia_entre_rectasH))
                ventana.blit(text, textRect)

                contadorV += 1





    pygame.display.update()

pygame.quit()