"""
Author: Aleksa Zatezalo
Date: December 2023
Description: Package to create nodes in a Huffman tree during decompression.
"""

class HuffmanNode:
    """
    A class that represents a node in a huffman tree.
    """
    
    def __init__(self, value, frequency, left=0, right=0):
        self.value = 0
        self.frequency = 0
        self.left = 0
        self.right = 0

    def set_left(self, node):
        self.left = node

    def get_left(self):
        return self.left

    def set_right(self, node):
        self.right = node
    
    def get_right(self):
        return self.right

    def set_value(self, num):
        self.value = num

    def get_value(self):
        return self.value

    def set_frequency(self, num):
        self.frequency = num
    
    def get_frequency(self):
        return self.frequency
    
    def is_leaf(self):
        return self.left & self.right
