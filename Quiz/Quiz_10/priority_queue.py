# Written by Mingkai Ma for COMP9021


from binary_tree import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()
        self.data = [None]
        self.nb_of_elements = 0

    def insert(self, value):
        self.nb_of_elements += 1
        self.data.append(value)
        self._bubble_up(self.nb_of_elements)
        self._transfer_to_tree()

    def _bubble_up(self, position):
        if position == 1:
            return
        elif self.data[position] < self.data[position // 2]:
            self.data[position], self.data[position // 2] = self.data[position // 2], self.data[position]
            self._bubble_up(position // 2)

    def _transfer_to_tree(self):

        L = self.data[1:]
        tree_L = []
        for i in L:
            tree_L.append(BinaryTree(i))

        max_value = len(L)

        for i in range(len(L)):
            if 2 * i + 1 < max_value:
                left_tree = tree_L[2 * i + 1]
                tree_L[i].left_node = left_tree
            if 2 * i + 2 < max_value:
                right_tree = tree_L[2 * i + 2]
                tree_L[i].right_node = right_tree

        self.value = tree_L[0].value
        self.left_node = tree_L[0].left_node
        self.right_node = tree_L[0].right_node
        
        
                
    
        
    
        

