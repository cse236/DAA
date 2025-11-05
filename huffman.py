import heapq
from collections import Counter

# Node structure for Huffman Tree
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heapq to compare nodes
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(text):
    frequency = Counter(text)  # Count frequency of each character
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)  # Min-heap based on frequency

    while len(heap) > 1:
        # Extract two nodes with smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge nodes
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # Root node

# Function to generate Huffman Codes
def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if node is None:
        return code_map

    if node.char is not None:  # Leaf node
        code_map[node.char] = prefix or "0"  # handle single char edge case

    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)
    return code_map

# Function to encode text
def huffman_encode(text):
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

# Function to decode text
def huffman_decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_text = ""
    temp = ""
    for bit in encoded_text:
        temp += bit
        if temp in reverse_codes:
            decoded_text += reverse_codes[temp]
            temp = ""
    return decoded_text

# Driver code
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    print("Original Text:", text)
    print()
    encoded_text, codes = huffman_encode(text)
    print("Huffman Codes:", codes)
    print()
    print("Encoded Text:", encoded_text)
    print()
    decoded_text = huffman_decode(encoded_text, codes)
    print("Decoded Text:", decoded_text)
