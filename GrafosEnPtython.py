class Graph:
    def __init__(self):
        self.graph = {}

    # Crear (Agregar nodo y arista)
    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    # Leer (Mostrar las conexiones de un nodo)
    def get_connections(self, node):
        return self.graph.get(node, [])

    # Actualizar (Agregar un vecino adicional a un nodo)
    def update_edge(self, node, old_neighbor, new_neighbor):
        if node in self.graph and old_neighbor in self.graph[node]:
            self.graph[node].remove(old_neighbor)
            self.graph[node].append(new_neighbor)

    # Eliminar (Eliminar un nodo y sus conexiones)
    def delete_node(self, node):
        if node in self.graph:
            del self.graph[node]
        for connections in self.graph.values():
            if node in connections:
                connections.remove(node)

    # Mostrar el grafo completo
    def display_graph(self):
        return self.graph

# Uso
g = Graph()
g.add_edge("0: Manizales", "1: Pereira")
g.add_edge("0: Manizales", "2: Armenia")
g.add_edge("0: Manizales", "3: Chinchina ")
g.add_edge("0: Manizales", "4: Villamaria")
g.add_edge("0: Manizales", "5: Palestina")
g.add_edge("0: Manizales", "6: Neira")
g.add_edge("0: Manizales", "8: Dosquebradas")
g.add_edge("0: Manizales", "9: Santa Rosa de Cabal")
g.add_edge("0: Manizales", "10: Cartago")


g.add_edge("1: Pereira", "0: Manizales")
g.add_edge("1: Pereira", "2: Armenia")
g.add_edge("1: Pereira", "7: La Virginia")
g.add_edge("1: Pereira", "8: Dosquebradas")
g.add_edge("1: Pereira", "9: Santa Rosa de Cabal")
g.add_edge("1: Pereira", "10: Cartago")
g.add_edge("1: Pereira", "12: Ciscasia")

g.add_edge("2: Armenia", "0: Manizales")
g.add_edge("2: Armenia", "1: Pereira")
g.add_edge("2: Armenia", "8: Dosquebradas")
g.add_edge("2: Armenia", "9: Santa Rosa de Cabal")
g.add_edge("2: Armenia", "10: Cartago")
g.add_edge("2: Armenia", "11: Calarca)")
g.add_edge("2: Armenia", "12: Ciscasia")
g.add_edge("2: Armenia", "13: La Tebaida")
g.add_edge("2: Armenia", "14: Montenegro")

g.add_edge("3: Chinchina", "0: Manizales")


g.add_edge("4: Villamaria", "0: Manizales")


g.add_edge("5: Palestina", "0: Manizales")


g.add_edge("6: Neira", "0: Manizales")

g.add_edge("7: La Virginia", "1: Pereira")
g.add_edge("7: La Virginia", "10: Cartago")

 
g.add_edge("8: Dosquebradas", "0: Manizales")
g.add_edge("8: Dosquebradas", "1: Pereira")
g.add_edge("8: Dosquebradas", "2: Armenia")
g.add_edge("8: Dosquebradas", "10 :Cartago")

 
g.add_edge("9: Santa Rosa de Cabal", "0: Manizales")
g.add_edge("9: Santa Rosa de Cabal", "1: Pereira")
g.add_edge("9: Santa Rosa de Cabal", "2: Armenia")


g.add_edge("10: Cartago", "0: Manizales")
g.add_edge("10: Cartago", "1: Pereira")
g.add_edge("10: Cartago", "2: Armenia")
g.add_edge("10: Cartago", "7: La Virginia")
g.add_edge("10: Cartago", "8: Dos quebradas")

g.add_edge("11: Calarca", "2: Armenia")

g.add_edge("12: Ciscasia", "2: Armenia")

g.add_edge("13: La Tebaida", "2: Armenia")

g.add_edge("14: Montenegro", "2: Armenia")

print("Grafo completo:", g.display_graph())

print("Conexiones de Manizales: ", g.get_connections("0: Manizales"))

print("Conexiones de Pereira: ", g.get_connections("1: Pereira"))

print("Conexiones de Armenia: ", g.get_connections("2: Armenia"))

print("Conexiones de Chinchina: ", g.get_connections("3: Chinchina"))

print("Conexiones de Villamaria: ", g.get_connections("4: Villamaria"))

print("Conexiones de Palestina: ", g.get_connections("5: Palestina"))

print("Conexiones de Neira: ", g.get_connections("6: Neira"))

print("Conexiones de La Virginia: ", g.get_connections("7: La Virginia"))

print("Conexiones de Dosquebradas: ", g.get_connections("8: Dosquebradas"))

print("Conexiones de Santa Rosa de Cabal: ", g.get_connections("9: Santa Rosa de Cabal"))

print("Conexiones de Cartago", g.get_connections("10: Cartago"))

print("Conexiones de Calarca: ", g.get_connections("11: Calarca"))
 
print("Conexiones de Ciscasia: ", g.get_connections("12: Ciscasia"))
 
print("Conexiones de La Tebaida: ", g.get_connections("13: La Tebaida"))
 
print("Conexiones de Montenegro: ", g.get_connections("14: Montenegro"))
