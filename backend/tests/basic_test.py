from unittest import TestCase

from huffman_coding import HuffmanCoding
from huffman_node import HuffmanNode

class FunctionTest:
    def setUp(TestCase) -> None:
        return super().setUp() 
    def test_encode_decode(self):
        text = "computer"
        tree, encoded = HuffmanCoding.encode(text)
        decoded = HuffmanCoding.decode(tree, encoded)

        self.assertEqual(text, decoded)