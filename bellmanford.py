"""
VERSION 1.1
29 ABRIL 2018
"""

def bellman_ford(grafo, nodoInicial):
	"""Calcula la ruta más corta entre todos los nodos.

	RECIBE: str(nodo inicial) y un grafo(diccionario).
	DEVUELVE: Un diccionario con las rutas y pesos.

	ALGORITMO DE BELLMAN-FORD:

	Llamamos nodo inicial a aquel en el que se inicia la búsqueda,
	distancia del nodo a la distancia desde el nodo inicial hasta
	el nodo actual y predecesor al nodo desde el cual se llega al nodo
	actual con el camino de menor peso.

	1. Asignar a cada nodo una distancia un nodo predecesor tentativos:
	(0 para el nodo inicial, 'inf para todos los nodos restantes);
	(predecesor nulo para todos los nodos)

	2. Repetir |V| - 1 veces

		(a) Para cada arista (u, v) con peso w:
			Si la distancia del nodo actual u sumada al peso w de la
			arista que llega a v es menor que la distancia tentativa al
			nodo v, sobreescribir la distancia a v con la suma mencionada
			y guardar a u como predecesor de v.

	3. Verificar que no existan ciclos de pesos negativos:

		(a) Para cada arista (u, v) con peso w:
			Si la distancia del nodo actual u sumada al peso w de la
			arista que llega a v es menor que la distancia tentativa al
			nodo v, devolver un mensaje de error indicando que existe
			un ciclo de peso negativo.
	"""
	nodosTabla = {}
	#1
	nodosTabla = {nodoInicial:[0,None]}
	for i in grafo: 
		if i != nodoInicial:
			nodosTabla[i] = [float('inf'),None]
	#2
	for x in range(0 , len(nodosTabla) - 1):
		for nodoActual in grafo:
			for v in grafo[nodoActual]:
				if (nodosTabla[nodoActual][0] + grafo[nodoActual][v]) < nodosTabla[v][0]:
					nodosTabla[v][0] = nodosTabla[nodoActual][0] + grafo[nodoActual][v]
					nodosTabla[v][1] = nodoActual

	#3
	for nodoActual in grafo:
			for v in grafo[nodoActual]:
				if (nodosTabla[nodoActual][0] + grafo[nodoActual][v]) < nodosTabla[v][0]:
					print('Existe un ciclo de peso negativo')
					exit()

	return nodosTabla