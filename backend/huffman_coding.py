from typing import Dict, Tuple
from huffman_node import HuffmanNode
from pri_queue import PriorityQueue

class HuffmanCoding:
    # Encodes a string and returns the huffman tree and the resulting binary sequence
    # as a string
    @staticmethod
    def encode(string)->Tuple[HuffmanNode, str]:
        return
    # Takes the huffman tree root and the encoded string and decodes the message
    @staticmethod
    def decode(huffman_tree:HuffmanNode, encoding:str):
        return
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
    