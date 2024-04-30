def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    vertices, aristas = grafo_lista
    grados = {}

    for vertice in vertices:
        grados[vertice] = 0

    for arista in aristas:
        origen, destino = arista
        grados[origen] += 1
        grados[destino] += 1

    for vertice, grado in grados.items():
        print(f'Grado de {vertice}: {grado}')

def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    vertices, aristas = grafo_lista
    grados = {}

    for vertice in vertices:
        grados[vertice] = 0

    for arista in aristas:
        origen, destino = arista
        grados[origen] += 1
        grados[destino] += 1

    aislados = []

    for vertice, grado in grados.items():
        if (grado == 0):
            aislados.append(vertice)

    return aislados

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    vertices, aristas = grafo_lista
    grados = {}

    for vertice in vertices:
        grados[vertice] = 0

    for arista in aristas:
        origen, destino = arista
        grados[origen] += 1
        grados[destino] += 1

    lista_conexos = []
    lista_aislados = []

    for vertice, grado in grados.items():
        if (grado == 0):
            lista_aislados.append(vertice)
        else:
            lista_conexos.append(vertice)

    resultado = []
    resultado = [lista_conexos, lista_aislados]

    return resultado

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    vertices, aristas = grafo_lista
    grados = {}

    for vertice in vertices:
        grados[vertice] = 0

    for arista in aristas:
        origen, destino = arista
        grados[origen] += 1
        grados[destino] += 1

    conexo = 0

    for vertice, grado in grados.items():
        if (grado == 0):
            conexo = 1
    
    if (conexo == 1):
        return False
    else:
        return True