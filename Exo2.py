from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Ajoute une arête entre les nœuds u et v (graphe non orienté)."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        """Parcours en largeur (BFS) à partir du nœud start."""
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph[node])  # Ajoute tous les voisins non visités

        return result

    def dfs(self, start, visited=None):
        """Parcours en profondeur (DFS) récursif à partir du nœud start."""
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))

        return result

    def are_connected(self, u, v):
        """Vérifie si deux localisations sont connectées dans le graphe."""
        return v in self.bfs(u)

    def shortest_path_bfs(self, start, target):
        """Trouve le plus court chemin entre start et target en utilisant BFS."""
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()
            if node == target:
                return path  # Retourne le chemin trouvé

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    queue.append((neighbor, path + [neighbor]))

        return None  # Aucun chemin trouvé

def main():
    # Création du graphe
    city_map = Graph()
    
    # Ajout des connexions (exemple de carte de ville)
    city_map.add_edge("A", "B")
    city_map.add_edge("A", "C")
    city_map.add_edge("B", "D")
    city_map.add_edge("C", "E")
    city_map.add_edge("D", "E")
    city_map.add_edge("E", "F")

    print("Parcours BFS depuis A :", city_map.bfs("A"))
    print("Parcours DFS depuis A :", city_map.dfs("A"))

    # Vérification de la connectivité
    print("A et F sont connectés ?", city_map.are_connected("A", "F"))
    print("A et Z sont connectés ?", city_map.are_connected("A", "Z"))  # Devrait être False

    # Recherche du plus court chemin
    print("Plus court chemin entre A et F :", city_map.shortest_path_bfs("A", "F"))

if __name__ == "__main__":
    main()
