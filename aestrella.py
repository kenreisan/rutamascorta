"""
VERSION 1.1
30 ABRIL 2018
"""

def a_estrella(grafo, inicio, objetivo):
	"""Calcula la ruta más corta entre dos nodos.

	RECIBE: str(nodo inicial), str(nodo objetivo) y un grafo(diccionario).
	DEVUELVE: Una lista con la ruta más corta entre los nodos.

	ALGORITMO A* (A ESTRELLA)

	Llamamos inicio a aquel nodo en el que se inicia la búsqueda, objetivo
	aquel al que se desea llegar y predecesor al nodo desde el cual se llega
	al nodo actual con el camino de menor peso. 

	1. Inicialización:
		
		Conjunto de nodos evaluados iniclamente vacío. Conjunto de nodos
		descubiertos pero que aún no han sido evaluados inicialmente sólo
		contiene a inicio (conjunto_abierto) 

		Predecesor nulo para todos los nodos. Asignar a cada nodo una distancia
		tentativa (g(n)) para llegar a ese nodo (0 para el nodo inicial, 'inf'
		para todos los nodos restantes) 

		Asignar a cada nodo una distancia tentativa (f(n)) para llegar al nodo
		destino con ayuda de la heurística (estimacion_heuristica (inicio, objetivo)
		para el nodo inicial y 'inf' para todos los nodos restantes)

	2. Mientras conjunto_abierto tenga elementos:

		actual <- nodo del conjunto abierto con la menor distancia tentativa heurística

		Si actual = objetivo
		Regresar reconstruir_camino(predecesor, actual)

		Sacar actual del conjunto_abierto

		Agregar actual al conjunto_cerrado

		Para cada vecino de actual:
			• Si vecino E conjunto_cerrado
			ignorar y pasar al siguiente vecino

			• Calcular distancia desde el inicio hasta el vecino:
			g_tentativa <- g(actual) + peso_arista(actual, vecino)

			• Si vecino -E conjunto_abierto -> nuevo nodo descubierto,
			agregar vecino al conjunto_abierto

			• Otro, si g_tentativa >= g(vecino) -> no hay mejora en el
			camino, ignorar y pasar al vecino siguiente

			• Este camino es mejor, guardarlo:
			predecesor(vecino) <- actual
			g(vecino) <- g_tentativa
			f(vecino) <- g(vecino) + estimacion_heuristica(vecino, objetivo)

	3. Regresar error
	"""
	#1
	setCerrado = []
	setAbierto = [inicio]
	nodosTabla = {}

	for nodo in grafo:
		if inicio == nodo:
			nodosTabla[nodo] = [0, grafo[nodo][0], None]
		else:
			nodosTabla[nodo] = [float('inf'),float('inf'), None]
	#2
	while len(setAbierto) != 0:

		actual = mejor_heuristica(nodosTabla,setAbierto)

		if actual == objetivo:
			#return reconstruir_camino(objetivo,nodosTabla)
			return nodosTabla
		else:
			setAbierto.remove(actual)
			setCerrado.append(actual)

		for vecino in grafo[actual][1]:
			if vecino in setCerrado:
				pass
			else:
				g_tentativa = nodosTabla[actual][0] + grafo[actual][1][vecino]
			
				if vecino not in setAbierto:
					setAbierto.append(vecino)

				if g_tentativa >= nodosTabla[vecino][0]:
					pass
				else:
					nodosTabla[vecino][0] = g_tentativa
					nodosTabla[vecino][1] = nodosTabla[vecino][0] + grafo[vecino][0]
					nodosTabla[vecino][2] = actual
	#3
	return 'Error'

def mejor_heuristica(nodeTable,openset):
	"""Elige el nodo del conjunto abierto con la menor distancia tentativa heuristica.

	RECIBE: Tabla con los calculos de nodos y el conjunto abierto.
	DEVUELVE: el nodo con la menor distancia heuristica.

	Compara la distancia heuristica entre los nodos y elige el nodo
	con la menor distancia.
	"""
	heuristica = float('inf')

	for nodo in openset:
		if heuristica > nodeTable[nodo][1]:
			heuristica = nodeTable[nodo][1]
			nodoSiguiente = nodo
	
	return nodoSiguiente

def reconstruir_camino(nodoDestino, nodeTable):
	"""Arma la ruta que se recorre del nodo inicial al nodo destino.

	RECIBE: str(nodo destino), diccionario con rutas y pesos calculados.
	DEVUELVE: una tupla con la ruta.

	Recorre la ruta calculada por el algoritmo de Bellman-Ford desde el
	nodo final hasta el nodo inicial.
	"""

	ruta = [nodeTable[nodoDestino][1], nodoDestino]
	nodoActual = nodoDestino
	
	while nodeTable[nodoActual][-1] != None:
		ruta.append(nodeTable[nodoActual][-1])
		nodoActual = nodeTable[nodoActual][-1]

	ruta.reverse()

	return ruta