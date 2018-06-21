"""
VERSION 1.0
23 ABRIL 2018
"""

def dijkstra(grafo,nodoInicial,nodoDestino):
  """Calcula la ruta más corta entre dos nodos.

  RECIBE: Un grafo(diccionario), el str(nodo inicial) y el str(nodo destino).
  DEVUELVE: un diccionario {nodo:peso} de todos los nodos existentes en el grafo.

  El peso de cada nodo representa la distancia más corta que se deberá recorrer
  para llegar a él desde el nodo marcado como inicial o origen, que se representa
  que en el diccionario devuelto se representa con un peso de cero {nodo:0}.

  ALGORITMO DE DIJKSTRA:

  Llamamos nodo inicial a aquel en el que se inicia la búsqueda, nodo destino a aquel
  al que se desea llegar y distancia del nodo a la distancia desde el nodo inicial
  hasta el nodo actual.

  1. Asignar a cada nodo una distancia tentativa: 0 para el nodo inicial,
  'inf' para todos los nodos restantes.

  2. Establecer al nodo inicial como nodo actual y crear un conjunto de nodos
  no visitados, llamado conjunto no visitado que contiene a todos los nodos 
  excepto al actual

  3. Para el nodo actual, considerar a todos sus vecinos no visitados y
  recalcular sus distancias tentativas:
  
  * Si la distancia del nodo actual sumada a la distancia desde el nodo
    actual hasta algún vecino es menor que la distancia tentativa actual
    de ese vecino, se debe sobreescribir la distancia con la suma obtenida.
    El nodo vecino aún no debe marcarse como visitado y se conserva dentro
    del conjunto no visitado.

  4. Cuando se termina de revisar a todos los vecinos del nodo actual, se
  marca como visitado y se elimina del conjunto no visitado: un nodo visitado
  no se revisará nuevamente.

  5. Si el nodo destino se ha marcado como visitado, el algoritmo ha terminado.
  Para obtener la ruta, se realiza la etapa regresiva: a partir del nodo 
  destino, recorrer la gráfica tomando el estado de peso mínimo. Si se desea
  obtener la ruta más corta desde el nodo inicial a todos los nodos de de la
  gráfica, se continúa la ejecución hasta vaciar al conjunto no visitado.

  6. Seleccionar el nodo no visitado con menor distancia tentativa y marcarlo
  como el nuevo nodo actual, regresar al paso 3.
  """

  #1,2
  nodosTabla = {}
  nodosNoVisitados = []

  nodoActual = nodoInicial
  nodosTabla[nodoActual] = [0,None]
  #nodosNoVisitados.append(nodoInicial)
  for nodo in grafo:
    if nodo != nodoActual:
      nodosTabla[nodo] = [float('inf'),None]
      nodosNoVisitados.append(nodo)

  #3
  while len(nodosNoVisitados) > 0:

    pesoMin = float('inf')

    for vertice in grafo[nodoActual]:
      if (nodosTabla[nodoActual][0] + grafo[nodoActual][vertice]) < nodosTabla[vertice][0]:
        nodosTabla[vertice][0] = (nodosTabla[nodoActual][0] + grafo[nodoActual][vertice])
        nodosTabla[vertice][1] = nodoActual

  #6
    if nodoActual in nodosNoVisitados:
      nodosNoVisitados.remove(nodoActual)

  #5
    for node in nodosNoVisitados:
      if pesoMin > nodosTabla[node][0]:
        pesoMin = nodosTabla[node][0]
        nodoActual = node
    
    if nodoDestino not in nodosNoVisitados:
      return nodosTabla
  
  return nodosTabla