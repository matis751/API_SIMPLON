import sys
sys.path.insert(0, '../main.py')
from main import Class

#A function that print the value of Nodes
def Tree_walk(node):
    if node != None:
        Tree_walk(node.left)
        print (node.key, node.word_occurence)
        Tree_walk(node.right)

#A fucntion that shearch for a node with the value key
def Tree_shearch(node, key):
    if node == None or key == node.key:
        return node
    if key < node.key:
        return(Tree_shearch(node.left, key))
    else:
        return(Tree_shearch(node.right, key))

#A fucntion that shearch for a node with the value key with a loop
def Iterative_tree_shearch(node, key):
    while node != None and key != node.key:
        if key < node.key:
            node = node.left
        else:
            node = node.right
    return node

#A function that insert a new node in a Tree
def Tree_insert(Tree, New_node):
    tmp = None
    if (Tree.root is not None):
        node = Tree.root
        while node is not None:
            tmp = node
            if New_node.key < node.key:
                node = node.left
            else:
                node = node.right
        New_node.precedent = tmp

    if tmp is None:
        Tree.root = New_node #L'arbre etait vide
    elif New_node.key < tmp.key:
        tmp.left = New_node
    else:
        tmp.right = New_node

