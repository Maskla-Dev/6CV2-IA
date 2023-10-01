import os
import networkx as nx
import matplotlib.pyplot as plt

def Grafo():
    G = nx.Graph()
    G.add_edge('a', 'p')
    G.add_edge('a', 'j')
    G.add_edge('a', 'b')
    G.add_edge('b', 'd')
    G.add_edge('b', 'e')
    G.add_edge('b', 'c')
    G.add_edge('j', 'a')
    G.add_edge('p', 'a')
    G.add_edge('d', 'b')
    G.add_edge('d', 'g')
    G.add_edge('e', 'b')
    G.add_edge('e', 'g')
    G.add_edge('e', 'f')
    G.add_edge('e', 'c')
    G.add_edge('c', 'b')
    G.add_edge('c', 'e')
    G.add_edge('c', 'f')
    G.add_edge('c', 'i')
    G.add_edge('g', 'd')
    G.add_edge('g', 'e')
    G.add_edge('g', 'f')
    G.add_edge('g', 'h')
    G.add_edge('f', 'g')
    G.add_edge('f', 'e')
    G.add_edge('f', 'c')
    G.add_edge('i', 'c')
    G.add_edge('h', 'g')

    pos = {1: (0, 0), 2: (-1, 0.3), 3: (2, 0.17), 4: (4, 0.255), 5: (5, 0.03)}

    nx.draw(G, with_labels=True, font_weight='bold', font_color='white')
    plt.show()
    pass

def recorrido():

    #DEFINE EL GRAFO O ARBOL USANDO UN DICCIONARIO DE PYTHON
    #PARA SU MEJOR COMPRESION, EL VERTICE a TIENE EL VALOR 'a': [('p', 4), ('j', 15), ('b', 1)]
    #INDICA QUE EL VERTICE 'a' ES ADYACENTE CON 'p', CON 'j' Y CON 'b'
    #CADA UNO CON SU RESPECTIVO PESO, AUNQUE EL PESO PARA HACER RECORRIDOS EN PROFUNDIDAD NO ES NECESARIO

    grafo = {'a': [('p', 4), ('j', 15), ('b', 1)],
             'b': [('a', 1), ('d', 2), ('e', 2), ('c', 3)],
             'j': [('a', 15)],
             'p': [('a', 4)],
             'd': [('b', 2), ('g', 3)],
             'e': [('b', 2), ('g', 4), ('f', 5), ('c', 2)],
             'c': [('b', 3), ('e', 2), ('f', 5), ('i', 20)],
             'g': [('d', 3), ('e', 4), ('f', 10), ('h', 1)],
             'f': [('g',10), ('e',5), ('c',5)],
             'i': [('c',20)],
             'h': [('g',1)]}


    #MUESTRA EL GRAFO ANTES DEL RECORRIDO
    print("Muestra el grafo antes del recorrido")

    for key, lista in grafo.items():
        print(key)
        print(lista)

    print()
    os.system("pause")

    visitados = []
    pila = []

    origen = input("Ingresa un nodo: ")
    print("\nLista de recorrido en anchura\n")
    #Paso 1: SE COLOCA EL VERTICE ORIGEN EN UNA PILA
    pila.append(origen)
    #Paso 2: MIENTRAS LA PILA NO ESTE VACIA
    while pila:
        #Paso 3: DESAPILAR UN VERTICE, ESTE SERA AHORA EL VERTICE ACTUAL
        actual = pila.pop()
        #FORMA ALTERNATIVA PARA DESAPILAR:
        #actual = pila[-1]
        #pila.remove(pila[-1])

        #Paso 4: SI EL VERTICE ACTUAL NO HA SIDO VISITADO
        if actual not in visitados:
            #Paso 5: PROCESAR (IMPRIMIR) EL VERTICE ACTUAL
            print("Vertice actual ->", actual)
            #Paso 6: COLOCAR EL VERTICE ACTUAL EN LA LISTA DE VISITADOS
            visitados.append(actual)

        #Paso 7: PARA CADA VERTICE QUE EL VERTICE ACTUAL TIENE COMO DESTINO, Y QUE NO HA SIDO VISITADO; AMPLIAR EL VERTICE
        for key, lista in grafo[actual]:
            if key not in visitados:
                pila.insert(0, key)

    print()
    os.system("pause")
    pass

recorrido()
Grafo()

