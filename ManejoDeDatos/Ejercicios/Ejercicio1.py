#Sumar en binario con tarjetas

#cada tarjeta tiene dos renglones, hay 3 tarjetas
#cada renglon es de qué numero leemos: si leemos 0 es el primer renglon, si leemos 1 es el segundo renglon
#cada renglon tiene tres lugares:
#el primero te dice que escribe
#el segundo te dice si se mueve (1) o no, a la derecha
#el tercer renglon te dice a que tarjeta va a leer ahora

listaTodo = []

lista10 = [0,0,2]
lista11 = [1,0,3]
lista20 = [0,1,1]
lista21 = [1,1,1]
lista30 = [1,1,1]
lista31 = [0,1,4]
lista40 = [1,0,3]
lista41 = [0,0,4]

#metamos las listas en su tarjetas (1,2,3) y luego esa en la listaTodo

auxiliar = [lista10, lista11]
listaTodo.append(auxiliar)

auxiliar = [lista20, lista21]
listaTodo.append(auxiliar)

auxiliar = [lista30, lista31]
listaTodo.append(auxiliar)

auxiliar = [lista40, lista41]
listaTodo.append(auxiliar)
#print(listaTodo)

#renombramos por facilidad

T = listaTodo

n1="01001"
n2="11110"

print(" ",n1, "\n+ ")
print(" ",n2)
print("---------")

#vemos que tenemos dos numeros que se leen de derecha a izquierda (las unidades estan a la derecha y centenas a la izquierda)
#pero los indices van de izquierda a derecha (de 0 a n) entonces volteamos los numeros por comodiad (AQUI INICIA LA SECCION SIN ERROR)

n11=""
n22=""

for i in range(0,len(n1)):
    n11= n11 + n1[len(n1)-i-1]
#print(n11)

for i in range(0,len(n2)):
    n22= n22 + n2[len(n2)-i-1]
#print(n22)

n1=n11
n2=n22

#asi el numero esta escrito al reves y al sumar podemos usar indices normales, empiezas a sumar por las unidades, luego decenas, etc. (AQUI TERMINA LA SECCION SIN ERROR)

listaDeNumeros=[n1,n2] #los metemos en una lista para poder ir iterando entre ellos
#print(lista)

n3=[0,0,0,0,0]
n3=[0 for i in range(0,max(len(n1),len(n2))+1)] #hacemos una lista donde vamos a guardar el resultado
#lo hacemos en lista para poder ir escribiendo el resultado del final de la lista al inicio
#igual que como escribes el resultado al sumar dos numeros: escribes primero las unidades que estan a la izquierda
#además le agregamos un espacio porque la suma de dos numeros pueden dar un digito más que los sumados: ejemplo 5+5=10 (un digito + un digito= puede dar algo de dos digitos)
#print(n3)


#hacemos indices para saber en que numero vamos, en que tarjeta,y donde lo vamos escribiendo

IndicedeTrarjeta=0 #va de 0 a 2 por ser 3 tarjetas
lugardeEscritura=0 #va de 0 a len(max(numeros)) para ver que numero voy leyendo y en que lugar voy escribiendo
IndiceDeNumeroleido=0 #aqui me refiero a si estoy leyendo el primer o segundo numero de mis binarios del input

while True:
    numero=listaDeNumeros[IndiceDeNumeroleido][lugardeEscritura]
    numero=int(numero)
    #T[i] es la tarjeta numero i
    #T[0][i] es si vio 1 o 0 el renglon
    #T[0][0][i] es que esta leyendo de ese renglon
    n3[len(n3)-lugardeEscritura]=T[IndicedeTrarjeta][numero][0]
    #le digo que de la primera tarjeta, vaya al renglon del numeor que vio y vea la primera entrada
    #y eso lo escriba en el lugar n-indicedeescritura de mi resultado
    if T[IndicedeTrarjeta][numero][1]==1:
        #esto me dice si me muevo o no, si sí es un 1
        lugardeEscritura+=1
        #no hay else porque si no se mueve no hago nada
    IndicedeTrarjeta=T[IndicedeTrarjeta][numero][2]-1
    if IndiceDeNumeroleido==0: #voy en el primer numero
        IndiceDeNumeroleido=1
    else: #entoncers voy en el segundo
        IndiceDeNumeroleido=0
    #ver lo que llevamos y hacemos en cada ciclo
    #print("numero",numero," Tarjeta:",IndicedeTrarjeta," lugar de escrito",lugardeEscritura, "IndiceDeNumero", IndiceDeNumeroleido)

    #cuando terminamos
    if lugardeEscritura>(len(n3)-2):
        if n3[1]==0 and IndicedeTrarjeta==3:
            n3[0]=1
        break

#de aqui en adelante no hay error. Simplemente tomo cada numero de la lista y lo pego a un string para tener el resultado de corrido
resultado=""
#print(n3)
for i in n3:
    resultado += str(i)
#print(resultado)