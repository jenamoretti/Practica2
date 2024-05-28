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

---------------------------------------------------- p 3
def valida_nodo_en_grafo(grafo_lista, nodo):
    '''
    Dado un grafo en representacion de lista, y un nodo, me devuelve True si el nodo está en el Grafo
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
	'F'
    Ejemplo formato salida: 
        False
    '''
    vertices = grafo_lista[0]

    return nodo in vertices

def encuentra_camino(grafo_lista, nodo_ini, nodo_fin):
    '''
    Dado un grafo en representacion de lista, el nodo inicial y final de un camino
    Me devuelve una lista con los vértices del camino, o vacio si no existe
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	a
	b
    Ejemplo retorno: 
        ['a','b','d','c','e','d','b']
    '''
    vertices, aristas = grafo_lista

    grafo = {vertice : [] for vertice in vertices}
    for arista in aristas:
        origen, destino = arista
        grafo[origen].append(destino)
        grafo[destino].append(origen)

    camino = []
    camino.append(nodo_ini)

    if nodo_ini == nodo_fin:
        return camino

    if nodo_ini not in vertices:
        return None

    for nodo in grafo_lista[nodo_ini]:
        if nodo not in grafo_lista:
            return None
        nuevo_camino = encuentra_camino(grafo_lista, nodo, nodo_fin)
        if nuevo_camino:
            return camino + nuevo_camino

def encuentra_camino_cerrado(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	a
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    pass

def encuentra_recorrido(grafo_lista, nodo_ini, nodo_fin):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	b
	f
    Ejemplo retorno: 
        ['b','c','d','e','c','f']
    '''
    pass

def encuentra_circuito(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['d','a','b','d','c','e','d']
    '''
    pass 	 	

def encuentra_camino_simple(grafo_lista, nodo_ini, nodo_fin):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d']
    '''
    pass

def encuentra_ciclo(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    pass

def determina_caminos(camino_lista):
    '''
    Dado una lista que representa un camino, camino cerrado, recorrido, circuito, camino simple o ciclo,
    me devuelva de qué se trata
    Ejemplo Entrada: 
        ['d','a','b','d','c','e','d']
    Ejemplo formato salida: 
        Circuito

    '''
    pass

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
