"""
Author: Aleksa Zatezalo
Date: December 2023
Description: A script that encodes and decodes files using python.
"""

import HufmanNode as HuffmanNode

"""
Code for compressing and decompressing using Huffman compression.
"""


# ====================
# Helper functions for manipulating bytes


def get_bit(byte, bit_num):
    """ Return bit number bit_num from right in byte.

    @param int byte: a given byte
    @param int bit_num: a specific bit number within the byte
    @rtype: int

    >>> get_bit(0b00000101, 2)
    1
    >>> get_bit(0b00000101, 1)
    0
    """
    return (byte & (1 << bit_num)) >> bit_num


def byte_to_bits(byte):
    """ Return the representation of a byte as a string of bits.

    @param int byte: a given byte
    @rtype: str

    >>> byte_to_bits(14)
    '00001110'
    """
    return "".join([str(get_bit(byte, bit_num))
                    for bit_num in range(7, -1, -1)])


def bits_to_byte(bits):
    """ Return int represented by bits, padded on right.

    @param str bits: a string representation of some bits
    @rtype: int

    >>> bits_to_byte("00000101")
    5
    >>> bits_to_byte("101") == 0b10100000
    True
    """
    return sum([int(bits[pos]) << (7 - pos)
                for pos in range(len(bits))])


# ====================
# Functions for compression


def make_freq_dict(text):
    """ Return a dictionary that maps each byte in text to its frequency.

    @param bytes text: a bytes object
    @rtype: dict{int,int}

    >>> d = make_freq_dict(bytes([65, 66, 67, 66]))
    >>> d == {65: 1, 66: 2, 67: 1}
    True
    """
    freq_dict = {}

    for byte in text:
        if byte in freq_dict:
            freq_dict[byte] += 1
        else:
            freq_dict[byte] = 1
    return freq_dict


def huffman_tree(freq_dict):
    """ Return the root HuffmanNode of a Huffman tree corresponding
    to frequency dictionary freq_dict.

    @param dict(int,int) freq_dict: a frequency dictionary
    @rtype: HuffmanNode

    >>> freq = {2: 6, 3: 4}
    >>> t = huffman_tree(freq)
    >>> result1 = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> result2 = HuffmanNode(None, HuffmanNode(2), HuffmanNode(3))
    >>> t == result1 or t == result2
    True
    """

    dup_freq_dict = {k: v for k, v in freq_dict.items()}

    # all the leaf nodes in the tree
    leaf_labels = set(dup_freq_dict.keys())

    # all the leaf nodes

    nodes = {symbol:HuffmanNode(symbol) for symbol in dup_freq_dict}

    current_label = max(leaf_labels) + 1


    while len(nodes) != 1:
        min_l = min(dup_freq_dict.items(), key=lambda x: x[1])
        del dup_freq_dict[min_l[0]]
        min_r = min(dup_freq_dict.items(), key=lambda x: x[1])
        del dup_freq_dict[min_r[0]]
        # create a new node
        new_node = HuffmanNode(None, nodes[min_l[0]], nodes[min_r[0]])
        del nodes[min_l[0]]
        del nodes[min_r[0]]
        dup_freq_dict[current_label] = min_l[1] + min_r[1]
        nodes[current_label] = new_node

        current_label += 1


    _, tree = nodes.popitem()

    return tree



def get_codes_recurse(tree, symbol_map, current_code):
    """ Get the codes of the tree
    :param tree: The tree
    :param symbol_map:  The symbol map
    :param current_code: The current code of the node
    :return:
    """
    if tree.is_leaf():
        symbol_map[tree.symbol] = current_code
    else:
        get_codes_recurse(tree.left, symbol_map, current_code+"0")
        get_codes_recurse(tree.right, symbol_map, current_code+"1")


def get_codes(tree):
    """ Return a dict mapping symbols from tree rooted at HuffmanNode to codes.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: dict(int,str)

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> d = get_codes(tree)
    >>> d == {3: "0", 2: "1"}
    True

    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(None, HuffmanNode(9), HuffmanNode(10))
    >>> tree = HuffmanNode(None, left, right)
    >>> d = get_codes(tree)
    >>> d == {3:"00", 2:"01", 9:"10", 10:"11"}
    True
    """
    symbol_map = {}
    if tree.is_leaf():
        symbol_map[tree.symbol] = '0'
    else:
        get_codes_recurse(tree, symbol_map, "")

    return symbol_map


# get the post order of the internal nodes
def number_nodes_recurse(tree, postorder):
    """
    get the node by postorder
    :param tree: The tree
    :param postorder: The list to hold the node
    :return:
    """
    if not tree.is_leaf():
        number_nodes_recurse(tree.left, postorder)
        number_nodes_recurse(tree.right, postorder)
        postorder.append(tree)

def number_nodes(tree):
    """ Number internal nodes in tree according to postorder traversal;
    start numbering at 0.

    @param HuffmanNode tree:  a Huffman tree rooted at node 'tree'
    @rtype: NoneType

    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(None, HuffmanNode(9), HuffmanNode(10))
    >>> tree = HuffmanNode(None, left, right)
    >>> number_nodes(tree)
    >>> tree.left.number
    0
    >>> tree.right.number
    1
    >>> tree.number
    2
    """
    postorder = []
    number_nodes_recurse(tree, postorder)

    # lable the tree
    for idx, node in  enumerate(postorder):
        node.number = idx

def avg_length(tree, freq_dict):
    """ Return the number of bits per symbol required to compress text
    made of the symbols and frequencies in freq_dict, using the Huffman tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: float

    >>> freq = {3: 2, 2: 7, 9: 1}
    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(9)
    >>> tree = HuffmanNode(None, left, right)
    >>> avg_length(tree, freq)
    1.9
    >>> freq = {2: 2}
    >>> tree = HuffmanNode(2)
    >>> avg_length(tree, freq)
    1.0
    """
    # construct the huffman tree
    symbol_map = get_codes(tree)

    total_length = 0.0

    for symbol in freq_dict:
        total_length += len(symbol_map[symbol]) * freq_dict[symbol]


    return total_length / sum(freq_dict.values())



def generate_compressed(text, codes):
    """ Return compressed form of text, using mapping in codes for each symbol.

    @param bytes text: a bytes object
    @param dict(int,str) codes: mappings from symbols to codes
    @rtype: bytes

    >>> d = {0: "0", 1: "10", 2: "11"}
    >>> text = bytes([1, 2, 1, 0])
    >>> result = generate_compressed(text, d)
    >>> [byte_to_bits(byte) for byte in result]
    ['10111000']
    >>> text = bytes([1, 2, 1, 0, 2])
    >>> result = generate_compressed(text, d)
    >>> [byte_to_bits(byte) for byte in result]
    ['10111001', '10000000']
    """

    bit_codes = [codes[symbol] for symbol in text]
    bits = ''.join(bit_codes)
    # padding 0s at right of bits

    compressed_text = [bits_to_byte(bits[i:i+8]) \
                       for i in range(0, len(bits), 8)]

    return bytes(compressed_text)


# recurse get the bytes of the tree
def tree_to_bytes_recurse(tree, tree_bytes):
    """
    gat the bytes of the tree
    :param tree:  The tree
    :param tree_bytes: The bytes of the tree
    :return:
    """
    if tree is not None and not tree.is_leaf():
        tree_to_bytes_recurse(tree.left, tree_bytes)
        tree_to_bytes_recurse(tree.right, tree_bytes)

        if tree.left.is_leaf():
            tree_bytes.append(0)
            tree_bytes.append(tree.left.symbol)
        else:
            tree_bytes.append(1)
            tree_bytes.append(tree.left.number)

        if tree.right.is_leaf():
            tree_bytes.append(0)
            tree_bytes.append(tree.right.symbol)
        else:
            tree_bytes.append(1)
            tree_bytes.append(tree.right.number)

def tree_to_bytes(tree):
    """ Return a bytes representation of the tree rooted at tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes

    The representation should be based on the postorder traversal of tree
    internal nodes, starting from 0.
    Precondition: tree has its nodes numbered.

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> number_nodes(tree)
    >>> list(tree_to_bytes(tree))
    [0, 3, 0, 2]
    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(5)
    >>> tree = HuffmanNode(None, left, right)
    >>> number_nodes(tree)
    >>> list(tree_to_bytes(tree))
    [0, 3, 0, 2, 1, 0, 0, 5]
    """
    tree_bytes = []
    tree_to_bytes_recurse(tree, tree_bytes)

    return bytes(tree_bytes)


def num_nodes_to_bytes(tree):
    """ Return number of nodes required to represent tree (the root of a
    numbered Huffman tree).

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes
    """
    return bytes([tree.number + 1])


def size_to_bytes(size):
    """ Return the size as a bytes object.

    @param int size: a 32-bit integer that we want to convert to bytes
    @rtype: bytes

    >>> list(size_to_bytes(300))
    [44, 1, 0, 0]
    """
    # little-endian representation of 32-bit (4-byte)
    # int size
    return size.to_bytes(4, "little")


def compress(in_file, out_file):
    """ Compress contents of in_file and store results in out_file.

    @param str in_file: input file whose contents we want to compress
    @param str out_file: output file, where we store our compressed result
    @rtype: NoneType
    """
    with open(in_file, "rb") as f1:
        text = f1.read()
    freq = make_freq_dict(text)
    tree = huffman_tree(freq)
    codes = get_codes(tree)
    number_nodes(tree)
    print("Bits per symbol:", avg_length(tree, freq))
    result = (num_nodes_to_bytes(tree) + tree_to_bytes(tree) +
              size_to_bytes(len(text)))
    result += generate_compressed(text, codes)
    with open(out_file, "wb") as f2:
        f2.write(result)


# ====================
# Functions for decompression


def generate_tree_general(node_lst, root_index):
    """ Return the root of the Huffman tree corresponding
    to node_lst[root_index].

    The function assumes nothing about the order of the nodes in the list.

    @param list[ReadNode] node_lst: a list of ReadNode objects
    @param int root_index: index in the node list
    @rtype: HuffmanNode

    >>> lst = [ReadNode(0, 5, 0, 7), ReadNode(0, 10, 0, 12), \
    ReadNode(1, 1, 1, 0)]
    >>> generate_tree_general(lst, 2)
    HuffmanNode(None, HuffmanNode(None, HuffmanNode(10, None, None), \
HuffmanNode(12, None, None)), \
HuffmanNode(None, HuffmanNode(5, None, None), HuffmanNode(7, None, None)))
    """

    nodes = {}

    for i in range(len(node_lst)):
        node = HuffmanNode(None)
        node.number = i
        nodes[i] = node

    for i in range(len(node_lst)):
        l_type = node_lst[i].l_type
        l_data = node_lst[i].l_data
        r_type = node_lst[i].r_type
        r_data = node_lst[i].r_data

        if l_type == 0:
            nodes[i].left = HuffmanNode(l_data)
        else:
            nodes[i].left = nodes[l_data]

        if r_type == 0:
            nodes[i].right = HuffmanNode(r_data)
        else:
            nodes[i].right = nodes[r_data]


    tree = nodes[root_index]
    return tree

def generate_tree_postorder(node_lst, root_index):
    """ Return the root of the Huffman tree corresponding
    to node_lst[root_index].

    The function assumes that the list represents a tree in postorder.

    @param list[ReadNode] node_lst: a list of ReadNode objects
    @param int root_index: index in the node list
    @rtype: HuffmanNode

    >>> lst = [ReadNode(0, 5, 0, 7), ReadNode(0, 10, 0, 12), \
    ReadNode(1, 0, 1, 0)]
    >>> generate_tree_postorder(lst, 2)
    HuffmanNode(None, HuffmanNode(None, HuffmanNode(5, None, None), \
HuffmanNode(7, None, None)), \
HuffmanNode(None, HuffmanNode(10, None, None), HuffmanNode(12, None, None)))
    """

    tree = None
    nodes = []

    for idx, read_node in enumerate(node_lst):
        l_type = read_node.l_type
        l_data = read_node.l_data
        r_type = read_node.r_type
        r_data = read_node.r_data

        node = HuffmanNode(None)

        if l_type == 0:
            node.left = HuffmanNode(l_data)
        else:
            node.left = nodes.pop(0)


        if r_type == 0:
            node.right = HuffmanNode(r_data)
        else:
            node.right = nodes.pop(0)

        nodes.append(node)

        if idx == root_index:
            tree = node

    return tree




def generate_uncompressed(tree, text, size):
    """ Use Huffman tree to decompress size bytes from text.

    @param HuffmanNode tree: a HuffmanNode tree rooted at 'tree'
    @param bytes text: text to decompress
    @param int size: how many bytes to decompress from text.
    @rtype: bytes
    """

    decompress_text = []

    byte_idx = 0
    # get the first byte's bits
    bits = byte_to_bits(text[byte_idx])
    bit_idx = 0

    byte_idx += 1


    while size:
        curr_node = tree

        while not curr_node.is_leaf():
            if bit_idx == 8:
                bits = byte_to_bits(text[byte_idx])
                byte_idx += 1
                bit_idx = 0
            bit = bits[bit_idx]
            bit_idx += 1
            if bit == '0':
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        decompress_text.append(curr_node.symbol)

        size -= 1

    return bytes(decompress_text)



def bytes_to_nodes(buf):
    """ Return a list of ReadNodes corresponding to the bytes in buf.

    @param bytes buf: a bytes object
    @rtype: list[ReadNode]

    >>> bytes_to_nodes(bytes([0, 1, 0, 2]))
    [ReadNode(0, 1, 0, 2)]
    """
    lst = []
    for i in range(0, len(buf), 4):
        l_type = buf[i]
        l_data = buf[i+1]
        r_type = buf[i+2]
        r_data = buf[i+3]
        lst.append(ReadNode(l_type, l_data, r_type, r_data))
    return lst


def bytes_to_size(buf):
    """ Return the size corresponding to the
    given 4-byte little-endian representation.

    @param bytes buf: a bytes object
    @rtype: int

    >>> bytes_to_size(bytes([44, 1, 0, 0]))
    300
    """
    return int.from_bytes(buf, "little")


def uncompress(in_file, out_file):
    """ Uncompress contents of in_file and store results in out_file.

    @param str in_file: input file to uncompress
    @param str out_file: output file that will hold the uncompressed results
    @rtype: NoneType
    """
    with open(in_file, "rb") as f:
        num_nodes = f.read(1)[0]
        buf = f.read(num_nodes * 4)
        node_lst = bytes_to_nodes(buf)
        # use generate_tree_general or generate_tree_postorder here
        tree = generate_tree_general(node_lst, num_nodes - 1)
        size = bytes_to_size(f.read(4))
        with open(out_file, "wb") as g:
            text = f.read()
            g.write(generate_uncompressed(tree, text, size))


# ====================
# Other functions


def traversal(tree, nodes_with_length, length):
    """
    traversal the tree
    :param tree: The tree
    :param nodes_with_length: The depth of the leaf node
    :param length: current depth of the path
    :return:
    """
    if tree is not None:
        traversal(tree.left, nodes_with_length, length+1)
        traversal(tree.right, nodes_with_length, length+1)
        if tree.is_leaf():
            nodes_with_length[tree.symbol] = (length, tree)



def improve_tree(tree, freq_dict):
    """ Improve the tree as much as possible, without changing its shape,
    by swapping nodes. The improvements are with respect to freq_dict.

    @param HuffmanNode tree: Huffman tree rooted at 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: NoneType

    >>> left = HuffmanNode(None, HuffmanNode(99), HuffmanNode(100))
    >>> right = HuffmanNode(None, HuffmanNode(101), \
    HuffmanNode(None, HuffmanNode(97), HuffmanNode(98)))
    >>> tree = HuffmanNode(None, left, right)
    >>> freq = {97: 26, 98: 23, 99: 20, 100: 16, 101: 15}
    >>> improve_tree(tree, freq)
    >>> avg_length(tree, freq)
    2.31
    """
    nodes_with_length = {}
    traversal(tree, nodes_with_length, 0)

    nodes = list(nodes_with_length.values())

    nodes.sort(key=lambda x: x[0], reverse=True)

    items = sorted(freq_dict.items(), key=lambda x: x[1])

    for i in range(len(items)):
        nodes[i][1].symbol = items[i][0]


# print(huffman_tree({2:2}))

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
