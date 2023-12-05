"""
Author: Aleksa Zatezalo
Date: December 2023
Description: A script that encodes and decodes files using python.
"""


##########################################
#  Helper Functions For Manipulating Bytes
##########################################

def get_bit(byte, bit_num):
    """
    Return bit number bit_num from right in byte.

    @param int byte: a given byte
    @param int bit_num: a specific bit number within the byte
    @rtype: int
    """
    
    return (byte & (1 << bit_num)) >> bit_num

def byte_to_bits(byte):
    """
    Return the representation of a byte as a string of bits.

    @param int byte: a given byte
    @rtype string
    """
    
    return "".join([str(get_bit(byte, range(7, -1, -1)))])

def bits_to_bytes(bits):
    """
    Return int represented by bits, padded on the right.

    @param str bits: a string representation of some bits
    @rtype: int
    """

    return sum([int(bits[pos]) << (7 - pos) for pos in range(len(bits))])

##########################################
#  Helper Functions For Compression
##########################################

def make_freq_dict(text):
    """
    Return a dictionary that maps each byte in the text to its frequency.

    @param bytes text: a bytes directory
    @rtype: dict{int, int}
    """

    freq_dic = {}
    for byte in text:
        if byte in freq_dic.keys():
            freq_dic[byte] += 1
        else:
            freq_dic[byte] = 1
    return freq_dic

def huffman_tree(freq_dict):
    """
    Return the root HuffmanNode of a Huffman tree corresponding
    to frequency dictionary freq_dict.

    @param dict(int,int) freq_dict: a frequency dictionary
    @rtype: HuffmanNode
    """
    # Make an Array of Tupples

    # Leafs

    # Internals

    # Root Node

    pass

def get_codes_recurse(tree, symbol_map, current_code):
    """
    Get the codes of the tree.

    @param tree: The tree
    @param symbol_map: The symbol map
    @param current_code: The current code of the node
    @return: null
    """

    pass

def get_codes(tree):
    """
    Retrun a dict mapping symbols from a tree rutted at HuffmanNode to codes.

    @param HuffmanNode tree: a Hufman tree rooted at node 'tree'
    @rtype: dic(int, str)
    """
    
    pass

def number_nodes_recurse(tree, postorder):
    """
    get the node by postorder
    :param tree: The tree
    :param postorder: The list to hold the node
    :return:
    """
    
    pass

def number_nodes(tree):
    """ 
    Number internal nodes in tree according to postorder traversal;
    start numbering at 0.

    @param HuffmanNode tree:  a Huffman tree rooted at node 'tree'
    @rtype: NoneType
    """

    pass

def avg_length(tree, freq_dict):
    """
    Return the number of bits per symbol required to compress text
    made of the symbols and frequencies in freq_dict, using the Huffman tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: float
    """
    
    pass

def generate_compressed(text, codes):
    """
    Return compressed form of text, using mapping in codes for each symbol.

    @param bytes text: a bytes object
    @param dict(int,str) codes: mappings from symbols to codes
    @rtype: bytes
    """

    pass

# recurse get the bytes of the tree
def tree_to_bytes_recurse(tree, tree_bytes):
    """
    gat the bytes of the tree
    :param tree:  The tree
    :param tree_bytes: The bytes of the tree
    :return:
    """

    pass

def tree_to_bytes(tree):
    """ 
    Return a bytes representation of the tree rooted at tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes

    The representation should be based on the postorder traversal of tree
    internal nodes, starting from 0.
    Precondition: tree has its nodes numbered.
    """

    pass


def num_nodes_to_bytes(tree):
    """ 
    Return number of nodes required to represent tree (the root of a
    numbered Huffman tree).

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes
    """

    pass

def size_to_bytes(size):
    """
    Return the size as a bytes object.

    @param int size: a 32-bit integer that we want to convert to bytes
    @rtype: bytes
    """

    pass

def compress(in_file, out_file):
    """
    Compress contents of in_file and store results in out_file.

    @param str in_file: input file whose contents we want to compress
    @param str out_file: output file, where we store our compressed result
    @rtype: NoneType
    """

    pass

##########################################
#  Helper Functions For Decompression
##########################################
def generate_tree_general(node_lst, root_index):
    """
    Return the root of the Huffman tree corresponding
    to node_lst[root_index].

    The function assumes nothing about the order of the nodes in the list.

    @param list[ReadNode] node_lst: a list of ReadNode objects
    @param int root_index: index in the node list
    @rtype: HuffmanNode
    """

    pass

def generate_tree_postorder(node_lst, root_index):
    """
    Return the root of the Huffman tree corresponding
    to node_lst[root_index].

    The function assumes that the list represents a tree in postorder.

    @param list[ReadNode] node_lst: a list of ReadNode objects
    @param int root_index: index in the node list
    @rtype: HuffmanNode
    """

    pass



def generate_uncompressed(tree, text, size):
    """
    Use Huffman tree to decompress size bytes from text.

    @param HuffmanNode tree: a HuffmanNode tree rooted at 'tree'
    @param bytes text: text to decompress
    @param int size: how many bytes to decompress from text.
    @rtype: bytes
    """

    pass

def bytes_to_nodes(buf):
    """
    Return a list of ReadNodes corresponding to the bytes in buf.

    @param bytes buf: a bytes object
    @rtype: list[ReadNode]
    """

    pass

def bytes_to_size(buf):
    """
    Return the size corresponding to the
    given 4-byte little-endian representation.

    @param bytes buf: a bytes object
    @rtype: int
    """

    pass

def uncompress(in_file, out_file):
    """
    Uncompress contents of in_file and store results in out_file.

    @param str in_file: input file to uncompress
    @param str out_file: output file that will hold the uncompressed results
    @rtype: NoneType
    """
    
    pass

##########################################
#  Other functions
##########################################

def traversal(tree, nodes_with_length, length):
    """
    traversal the tree
    :param tree: The tree
    :param nodes_with_length: The depth of the leaf node
    :param length: current depth of the path
    :return:
    """
    
    pass



def improve_tree(tree, freq_dict):
    """ Improve the tree as much as possible, without changing its shape,
    by swapping nodes. The improvements are with respect to freq_dict.

    @param HuffmanNode tree: Huffman tree rooted at 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: NoneType
    """

    pass

if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="huffman_pyta.txt")
    # TODO: Uncomment these when you have implemented all the functions
    import doctest
    doctest.testmod()

    import time

    mode = input("Press c to compress or u to uncompress: ")
    if mode == "c":
        fname = input("File to compress: ")
        start = time.time()
        compress(fname, fname + ".huf")
        print("compressed {} in {} seconds."
              .format(fname, time.time() - start))
    elif mode == "u":
        fname = input("File to uncompress: ")
        start = time.time()
        uncompress(fname, fname + ".orig")
        print("uncompressed {} in {} seconds."
              .format(fname, time.time() - start))
