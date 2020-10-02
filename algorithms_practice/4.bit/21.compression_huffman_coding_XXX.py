"""
Huffman coding is an efficient method of compressing data without losing information.
This algorithm analyzes the symbols that appear in a message.
Symbols that appear more often will be encoded as a shorter-bit string
while symbols that aren't used as much will be encoded as longer strings.
"""

from algorithms.compression import huffman_coding


#input file path
path = "/0.Python_lib/PRACTICE/4.bit/sample.txt"



h = huffman_coding(path)

output_path = h.compress()
h.decompress(output_path)