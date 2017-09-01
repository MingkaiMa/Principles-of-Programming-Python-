# Written by Mingkai Ma for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
    
    def rearrange(self):

        length = self._get_length()
        min_node = self._find_min()
        self._wrap_round()
        first_start_node = self._find_first_start(min_node)

        
        def fun(node, n):
            
            save_node = node.next_node.next_node
            next_node = node.next_node
            start_node = node.next_node.next_node.next_node
            
            node.next_node = start_node
            next_node.next_node = node
            new_node = save_node

            if n == 1:
                node.next_node = None
                return
                


            fun(new_node, n - 1)
        
        node = self.head

        while node:

            if node.next_node.value == min_node.value:

                self.head = node.next_node
                times = length // 2
                fun(node, times)
                
                break
            node = node.next_node
            


    def _find_min(self):
        node = self.head
        min_node = Node(1000)
        while node:
            if node.value < min_node.value:
                min_node = node
            node = node.next_node
        return min_node

    def _find_first_start(self,min_node):
        node = self.head
        first_start_node = Node()
        while node:
            if node.next_node.value == min_node.value:
                first_start_node = node.next_node.next_node.next_node
                break
            node = node.next_node
        return first_start_node

    def _get_length(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next_node
        return length


    def _find_first_start_index(self, min_node):
        index = 0
        node = self.head
        first_start_node_1 = Node()
        while node:
            if node.next_node.value == min_node.value:
                first_start_node_1 = node.next_node.next_node.next_node
                index = self.index_of_value(first_start_node_1.value)
                return index
            node = node.next_node

        
        



    def _wrap_round(self):
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = self.head
        
        

