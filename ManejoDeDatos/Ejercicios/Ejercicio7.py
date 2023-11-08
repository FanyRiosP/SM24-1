'''
Crear una clase a la que le ingreso una lista y cuando mando llamar esa clase (creo un objeto) 
ese objeto se añade a una cola.
Ese objeto tiene un valor, un antes y un después por estar en la cola.
El antes y después (si es el primero en la cola, el "antes" será el valor None -lo mismo que null- ) 
se alterarán de forma automática cada que creemos un nuevo objeto de esa clase. (Si añado un nuevo objeto, 
el que ya estaba será el "antes" de este nuevo, y este nuevo será el después del que ya estaba)
Y tendrá un método para consultar uno de los valores de los objetos en la cola, 
de forma que al buscarlo me dará los valores de cada objeto (en la cola) que tengo que recorrer hasta llegar al buscado.
'''