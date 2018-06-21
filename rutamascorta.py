# -*- coding: utf-8 *-*

"""
VERSION 1.0
06 MAYO 2018

Para usar el programa:
	Se necesitan especificar 4 parametros:
	archivo con el grafo, algoritmo a usar, nodo inicial y nodo destino.

	Los algoritmos disponibles son:
		dijkstra
		bellmanford
		a*

	Ejemplo:
	py rutamascorta.py    grafos/grafo.txt     dijkstra        A         X
	   [nombre progrma]  [dir y nom archivo]  [algoritmo] [nodo ini] [nodo fin]
"""


import sys
import dijkstra
import bellmanford
import aestrella

def reconstruir_ruta(nodoDestino, nodeTable):
	"""Arma la ruta que se recorre del nodo inicial al nodo destino.

	RECIBE: str(nodo destino), diccionario con rutas y pesos calculados.
	DEVUELVE: una tupla con la ruta y peso total.
	"""

	ruta = [nodeTable[nodoDestino][0], nodoDestino]
	nodoActual = nodoDestino
	
	while nodeTable[nodoActual][-1] != None:
		ruta.append(nodeTable[nodoActual][-1])
		nodoActual = nodeTable[nodoActual][-1]

	ruta.reverse()

	return ruta

def escribir_ruta(nodoI, nodoF, ruta):
  """Imprime la ruta generada desde el nodo inical al nodo destino.
  
  RECIBE: el nodo inicial, nodo destino, diccionario de distancias finales
  asi como la lista con la ruta generada.
  DEVUELVE: Una cadena de texto con los datos obtenidos.  
  """

  escribir = '\nLa ruta del nodo ' + nodoI + ' al nodo ' + nodoF + ' es:\n\t' + nodoI
  
  for n in range(1, len(ruta) - 1):
    escribir = escribir + ' -> ' + ruta[n]

  escribir = escribir + '\n\tCon una distancia de: ' + str(ruta[-1])
  
  return escribir

def archivo_leer_h(archivo):
	"""Captura la informacion de un archivo con heuristica en un diccionario.

	RECIBE: Un archivo con el formato siguiente:
	[v1] -> [h(v1)] -> [a1(N1)] : [w(a)] , ... , [am(N1)] : [w(am)]
	[v2] -> [h(v2)] -> [a1(N2)] : [w(a)] , ... , [am(N2)] : [w(am)]
	   :																					:
	[vn] -> [h(vn)] -> [a1(Nn)] : [w(a)] , ... , [am(Nn)] : [w(am)]

	donde:
		h = heuristica
		v = nodo o vertice
		a = nodo o vertice adyacente
		w = peso arista

	DEVUELVE: Un diccionario con los datos del archivo.
	"""
	dicH = {}

	f = open(archivo, 'r')
	texto = f.read().replace(' ', '')
	linea = texto.split()
	f.close()

	#print(linea)
	for token in linea:
		n1 = token.split('->')
		dicH[n1[0]] = [float(n1[1]),{}]
		#print(n1[1])

		for subtoken in n1:
			n2 = subtoken.split(',')

			for subsubtoken in n2:
				n3 = subsubtoken.split(':')
				
				if n1[0] == n3[0] or n1[1] == n3[0]:
					pass
				
				else:
					dicH[n1[0]][1][n3[0]] = float(n3[-1])
	
	return dicH


def archivo_leer(archivo):
	"""Captura la informacion de un archivo en un diccionario.

	RECIBE: Un archivo con el formato siguiente:
	[v1] -> [a1(N1)] : [w(a)] , ... , [am(N1)] : [w(am)]
	[v2] -> [a1(N2)] : [w(a)] , ... , [am(N2)] : [w(am)]
	   :
	[vn] -> [a1(Nn)] : [w(a)] , ... , [am(Nn)] : [w(am)]

	donde:
		v = nodo o vertice
		a = nodo o vertice adyacente
		w = peso arista

	DEVUELVE: Un diccionario con los datos del archivo.
	"""
	diccionario = {}

	f = open(archivo, 'r')
	texto = f.read().replace(' ', '')
	f.close()

	linea = texto.split()

	for token in linea:
		n1 = token.split('->')
		diccionario[n1[0]] = {}

		for subtoken in n1:
			n2 = subtoken.split(',')

			for subsubtoken in n2:
				n3 = subsubtoken.split(':')

				if n1[0] == n3[0]:
					pass
				else:
					diccionario[n1[0]][n3[0]] = int(n3[-1])

	return diccionario


if __name__ == "__main__":

	try:
		archivo = str(sys.argv[1])
		algoritmo = str(sys.argv[2])
		nodoInicial = str(sys.argv[3])
		nodoDestino = str(sys.argv[4])
		
		if algoritmo == 'dijkstra':
			grafo = archivo_leer(archivo)
			print('\nALGORITMO DIJKSTRA:')
			print(escribir_ruta(nodoInicial, nodoDestino, reconstruir_ruta(nodoDestino, dijkstra.dijkstra(grafo,nodoInicial,nodoDestino))))
			print('\n')
			#print(dijkstra.dijkstra(grafo,nodoInicial,nodoDestino))

		elif algoritmo == 'bellmanford':
			grafo = archivo_leer(archivo)
			print('\nALGORITMO BELLMAN-FORD:')
			print(escribir_ruta(nodoInicial, nodoDestino, reconstruir_ruta(nodoDestino, bellmanford.bellman_ford(grafo,nodoInicial))))
			print('\n')
			#print(bellmanford.bellman_ford(grafo,nodoInicial))

		elif algoritmo == 'a*':
			grafo = archivo_leer_h(archivo)
			print('\nALGORITMO A*:')
			print(escribir_ruta(nodoInicial, nodoDestino, reconstruir_ruta(nodoDestino, aestrella.a_estrella(grafo,nodoInicial,nodoDestino))))
			print('\n')
			print(aestrella.a_estrella(grafo,nodoInicial,nodoDestino))

		else:
			print('Error en el nombre del algoritmo: {' + algoritmo + '}')

	except OSError:
		print("No se puedo abrir el archivo: ", archivo)

	except IndexError:
		print('No se proporcionaron los argumentos necesarios...')

	except KeyError:
		print('Hubo un error al procesar el algoritmo:\n', sys.exc_info()[0], sys.exc_info()[1])

	except ValueError:
		print('Hubo un error al procesar el algoritmo:\n', sys.exc_info()[0], sys.exc_info()[1])
	
	