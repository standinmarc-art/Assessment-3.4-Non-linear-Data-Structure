from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # BFS (Level Order Traversal)
    def bfs(self):
        if not self.root:
            return
        queue = deque()
        queue.append(self.root)
        print("BFS:", end=" ")
        while queue:
            current = queue.popleft()
            print(current.value, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print("\n")

    # DFS (Pre-order Traversal)
    def dfs(self, node):
        if not node:
            return
        print(node.value, end=" ")
        self.dfs(node.left)
        self.dfs(node.right)


# ===== BUILD TREE & RUN =====
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node('M')
    tree.root.left = Node('E')
    tree.root.right = Node('D')
    tree.root.left.left = Node('I')
    tree.root.left.right = Node('C')
    tree.root.right.left = Node('O')

    tree.bfs()

    print("DFS:", end=" ")
    tree.dfs(tree.root)
    print()
