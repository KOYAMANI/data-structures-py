from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    
def dfs(node):
    if node is None:
        return
    print(node.data)
    dfs(node.left)
    dfs(node.right)
    

def bfs(node):
    if node is None:
        return
    queue = deque([node])
    
    while queue:
        node = queue.popleft()
        print(node.data)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    

root = Node(4)
root.insert(3)
root.insert(1)
root.insert(2)
root.insert(5)

print("DFS")
dfs(root)
print("BFS")
bfs(root)