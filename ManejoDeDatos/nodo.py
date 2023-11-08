#Un arbol esta hecho de nodos
#definimos una clase para crear nodos
#cada nodo tiene: valor, padre e hijos como caracteristicas


class Nodo(object):
    def __init__(self):
        self.valor=0
        self.padre= None
        self.hijos = []
        pass  # creando atributos

    def Modificar_padre(self,NodoPadre):
        self.padre = NodoPadre
        pass
    def Añadir_hijo(self,Nodohijo):
        self.hijos.append(Nodohijo)
        pass
    def Modificar_valor(self,valornuevo):
        self.valor = valornuevo
    def MostrarHijos(self):
        if self.hijos != []:
                print([i.valor for i in self.hijos])
        else:
            print("no hay hijos")
    def MostrarPadre(self):
        if self.padre != None:
            print(self.padre.valor)
        else:
            print("es la raiz o no tiene padre asignado")
x=Nodo()
x.Modificar_valor(10)
y=Nodo()
x.Añadir_hijo(y)
y.Modificar_padre(x)
y.Modificar_valor(15)
z=Nodo()
x.Añadir_hijo(z)
z.Modificar_padre(x)
z.Modificar_valor(12)

for i in range(5):
    k=Nodo()
    k.Modificar_valor(i)
    indice = i%2
    if indice ==0:
        y.Añadir_hijo(k)
        k.Modificar_padre(y)
    else:
        z.Añadir_hijo(k)
        k.Modificar_padre(z)


x.MostrarHijos()
y.MostrarHijos()
z.MostrarHijos()

x.MostrarPadre()
y.MostrarPadre()
z.MostrarPadre()