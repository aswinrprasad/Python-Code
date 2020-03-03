class Tree:
    def __init__(self, val):
        self.data, self.right, self.left = val, None, None
    
def insert(root, node):
    if root is None :
        root = node
    else:
        if root.data > node.data :
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)
        else :
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        
def inorder(root) :
    if root.left != None:
        inorder(root.left)
    print root.data,
    if root.right != None:
        inorder(root.right)
    return ""
    


nodes = map(int, raw_input("Enter the nodes you want to insert : ").split())
f=0
for i in nodes :
    if f == 0 :
        root = Tree(i)
        f=1
    else:
        insert(root, Tree(i))

print "The nodes in inorder traversal are :", inorder(root),