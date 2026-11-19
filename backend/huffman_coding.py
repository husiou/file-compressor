from typing import Dict, Tuple
from huffman_node import HuffmanNode
from pri_queue import PriorityQueue

class HuffmanCoding:
    # Encodes a string and returns the huffman tree and the resulting binary sequence
    # as a string
    @staticmethod
    def encode(string)->Tuple[HuffmanNode, str]:
        pri_queue = HuffmanCoding._generate_priority_queue(string)
        huff_tree = HuffmanCoding._generate_huffman_tree(pri_queue)
        char_codes = HuffmanCoding._get_char_codes(huff_tree)

        encoded_string = ""
        for char in string:
            encoded_string += char_codes[char]
        return huff_tree, encoded_string
    # Takes the huffman tree root and the encoded string and decodes the message
    @staticmethod
    def decode(huffman_tree:HuffmanNode, encoding:str)->str:
        decoded_string = ""
        cur_node = huffman_tree
        for num in encoding:
            if num == "0":
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
            if cur_node.left is None and cur_node.right is None:
                decoded_string += cur_node.value
                cur_node = huffman_tree
        return decoded_string
    # Builds a priority queue from the characters in the input_string, where the priority is
    # based on how many times a character appears. Smaller counts should come off the pqueue first.
    @staticmethod
    def _generate_priority_queue(input_string:str)->PriorityQueue:
        return
    # Builds a Huffman tree based on a priority queue using the Huffman Algorithm.
    # Dequeue 2 items at a time from the pqueue, put them under a new node, then enqueue the new node.
    # Repeat until you have only 1 node. 
    @staticmethod
    def _generate_huffman_tree(pqueue:PriorityQueue)->HuffmanNode:
        return
    # Traverses the Huffman tree to find the binary codes for each character and returns
    # a dictionary of codes for each character
    @staticmethod
    def _get_char_codes(huffman_tree_root:HuffmanNode)->Dict:
        return
    