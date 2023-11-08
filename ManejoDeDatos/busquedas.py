
def busqueda_lineal(secuencia, elemento):
    for indx, x in enumerate(secuencia):
        if elemento == x:
            return indx
    return None

def busqueda_binaria(secuencia, elemento, min, max):
    if min > max:
        return -1
    else:
        mid = (min + max) // 2
        if elemento == secuencia[mid]:
            return mid
        elif secuencia[mid] > elemento:
            return busqueda_binaria(secuencia, elemento, min, mid-1)
        else:
            return busqueda_binaria(secuencia, elemento, mid+1, max)
        