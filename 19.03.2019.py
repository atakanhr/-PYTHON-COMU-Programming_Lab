class Node(object):
    def __init__(self, v=0):
        self.value = v
        self.left = None
        self.right = None
class Tree(object):
    def __init__(self):
        self.root = Node(250)
        
    def insert(self, node_1):
        iter = ''
        if self.root.value > node_1.value :
            self.root.left = node_1
        elif self.root.value < node_1.value :
            self.root.right = node_1
        else:
            print('Duplicate error')
    
    def search(self, node):
        pass
    
    def remove(self, node):
        pass
    
    def printTree(self):
        Tree.printHelper(self.root)
    
    def printHelper(node):
        if node.left != None:
            Tree.printHelper(node.left)
        print(node.value)
        if node.right != None:
            Tree.printHelper(node.right)
tree_1 = Tree()  # root = 250
tree_1.insert(Node(-100))
tree_1.insert(Node(100))
tree_1.insert(Node(200))
tree_1.insert(Node(50))
tree_1.insert(Node(30))
tree_1.insert(Node(160))
# print(tree_1.root.value)
# print(tree_1.root.left.value)
# print(tree_1.root.right.value)
tree_1.printTree()   # L N R
