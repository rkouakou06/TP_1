# encoding : utf8
""" This script aims to show a binary tree. It also allows to display the
tree in a tree-like way by making a display of a path in depth. """

class Binary_tree():
    def __init__(self) -> None:
        self.root=None
        self.node = None

    def print_tree(self):
        """ Displays the node and all its descendants horizontally """
        return self.root.display_node()

    def print_tree_vertical(self):
        """ Displays the node and all its descendants vertically """
        return self.root.display_node_vertical()

class Node():
    """ Class allowing to create nodes as well as to add nodes to them (left or right) """
    def __init__(self, value):
        self.value=value
        self.right= None
        self.left= None
        self.depth= 0

    def add(self, left = None, right = None):
        """ This method allows to add nodes (left and/or right) to a node using recursion """
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        """ This method allows to update the depth
        of the added nodes (left and/or right) using recursion """
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    def display_node(self, level=0): #creation of a level counter that starts at 0
        """ This method allows to display each node
        and all its descendants in a "horizontal" way using recursion """
        retour = str(self)
        if self.right:
            retour += "\n"
            for _ in range(0,level+1): #add a tab at each level of the tree
                retour += "\t"
            retour += self.right.display_node(level+1) #add a right node at each level
        if self.left:
            retour += "\n"
            for _ in range(0,level+1): #add a tab at each level of the tree
                retour += "\t"
            retour += self.left.display_node(level+1) #add a left node at each level
        return retour

    def display_node_vertical(self, level=1):
        #counter at 1 because we want the first node not to start at the beginning of the chain
        """ This method allows to display the tree in a "vertical" way.
        This method is not fully functional."""
        retour = ""
        for _ in range(0,level):
            retour += "\t"
        retour += str(self)
        if self.left and self.right:
            #if the node has descendants in the left node and in the right node
            retour += "\n"
            retour += self.left.display_node_vertical(level-1)
            #we set level-1 so that when displayed, it is placed before its parent node
            retour += self.right.display_node_vertical(level+1)
        if self.left and self.right is None:
            #if the node has only one left node
            retour += "\n"
            retour += self.left.display_node_vertical(level+1)
        if self.left is None and self.right :
            #if the node has only one right node
            retour += "\n"
            retour += self.right.display_node_vertical(level+1)
        return retour

    def __str__(self):
        """ This method displays each node and its depth """
        return str(self.value) + "/" + str(self.depth)

    def is_leaf(self):
        """ This method allows to know if a node
        is a terminal node (leaf) or not """
        return not(self.left or self.right)

    # def get_max_depth(self,max_depth=0):
    #     """ This method allows to know the greatest depth in the tree."""
    #     if self.is_leaf():
    #         if self.depth > max_depth:
    #             return self.depth
    #         else:
    #             return max_depth
    #     # je suis le node d'un arbre
    #     else:
    #         if self.right:
    #             max_depth = self.right.get_max_depth(max_depth)

    #         if self.left:
    #             max_depth = self.left.get_max_depth(max_depth)
    #         return max_depth


if __name__ == "__main__":
    node1 = Node(0)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node3.add(node4)
    node1.add(node2, node3)
    tree1 = Binary_tree()
    tree1.root=node1

    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node5.add(node6, node7)
    node4.add(node5)
    node8 = Node(8)
    node7.add(node8)

    print("Binary tree with horizontal display\n ")
    print(tree1.print_tree())
    print("\nBinary tree with vertical display\n ")
    print(tree1.print_tree_vertical())
