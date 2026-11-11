from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # BFS
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        print("BFS:", end=" ")
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print("\n")

    # DFS
    def dfs(self, start):
        visited = set()
        print("DFS:", end=" ")
        self._dfs_helper(start, visited)
        print()

    def _dfs_helper(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.adj[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

# ===== BUILD GRAPH & RUN =====
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('M', 'E')
    graph.add_edge('M', 'D')
    graph.add_edge('E', 'I')
    graph.add_edge('E', 'C')
    graph.add_edge('D', 'O')
    graph.add_edge('I', 'C')

    graph.bfs('M')
    graph.dfs('M')
