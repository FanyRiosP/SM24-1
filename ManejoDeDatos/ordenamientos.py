# TIPOS DE ORDENAMIENTO

# Ordenamiento por selección

def seleccion(secuencia):
    n = len(secuencia)
    
    for pos in range(n):
        index_min = pos
        for j in range(pos+1, n): 
            if secuencia[j] < secuencia[index_min]:
                index_min = j
        if pos != index_min:
            aux = secuencia[pos]
            secuencia[pos] = secuencia[index_min]
            secuencia[index_min] = aux
    return secuencia

# Ordenamiento por insercion

def insercion(secuencia):
    for i in range(1, len(secuencia)):
        v = secuencia[i]
        j = i - 1
        while j >= 0 and v < secuencia[j]:
            secuencia[j + 1] = secuencia[j]
        secuencia[j + 1] = v
    return secuencia

# Ordenamiento de burbuja

def bubble_sort(secuencia):
    for j in range(len(secuencia) - 1, 0, -1):
        for i in range(1, j + 1):
            if secuencia[j - 1] > secuencia[i]:
                secuencia[i - j], secuencia[i] = secuencia[i], secuencia[i - 1]
    return secuencia

# Ordenamiento de mezcla

def merge_sort(l):
    if len(l) == 1 or l == []:
        return l
    l_izq = merge_sort(l[:len(l)//2])
    l_der = merge_sort(l[len(l)//2:])
    merge = []
    merged = False
    i_index = 0
    d_index = 0 
    while not merge:
        if l_izq[i_index] < l_der[d_index]:
            merge.append(l_izq[i_index])
            i_index += 1
        else:
            merge.append(l_der[d_index])
            d_index += 1
        
        if i_index == len(l_izq):
            merge.extend(l_der[d_index:])
            merge = True

        if d_index == len(l_der):
            merge.extend(l_izq[i_index:])
            merge = True
    return merge






