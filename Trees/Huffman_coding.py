import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(chars, freq):
    heap = []

    for char, f in zip(chars, freq):
        heapq.heappush(heap, Node(char, f))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    root = heap[0]
    codes = {}

    def generate_codes(node, code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code if code else "0"
            return
        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")
    generate_codes(root, "")
    return codes

n = int(input())
chars = input().split()
freq = list(map(int, input().split()))

codes = huffman_coding(chars, freq)

for char in chars:
    print(char, codes[char])