"""
霍夫曼编码是一种基于贪心算法的编码方式，通常用于无损数据压缩中。

在霍夫曼编码中，将出现频率较高的字符用较短的编码表示，而将出现频率较低的字符用较长的编码表示。
这样可以减少整个消息的编码长度，从而实现压缩。
"""

import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        # 用于优先队列中的比较，频率较小的节点优先级更高
        return self.freq < other.freq

def huffman_encoding(data):
    # 统计每个字符的频率
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    # 使用优先队列构建霍夫曼树
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=freq))

    while len(heap) > 1:
        # 取出频率最小的两个节点，合并为一个节点
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        merged_node = HuffmanNode(char=None, freq=left_node.freq + right_node.freq, left=left_node, right=right_node)
        # 将合并后的节点加入优先队列
        heapq.heappush(heap, merged_node)

    root_node = heap[0]

    # 生成霍夫曼编码表
    code_table = {}
    def generate_codes(node, code=''):
        if node.char:
            code_table[node.char] = code
        else:
            generate_codes(node.left, code + '0')
            generate_codes(node.right, code + '1')
    generate_codes(root_node)

    # 生成编码后的数据
    encoded_data = ''.join(code_table[char] for char in data)

    return encoded_data, code_table

def huffman_decoding(encoded_data, code_table):
    # 将霍夫曼编码表反转，方便后续解码
    decode_table = {code: char for char, code in code_table.items()}

    # 从编码后的数据中逐一解码出字符
    decoded_data = ''
    code_buffer = ''
    for bit in encoded_data:
        code_buffer += bit
        if code_buffer in decode_table:
            decoded_data += decode_table[code_buffer]
            code_buffer = ''

    return decoded_data


if __name__ == "__main__":

    data = 'aabbbccccddddeeeee'
    encoded_data, code_table = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, code_table)

    print(f'原始数据: {data}')
    print(f'编码后的数据: {encoded_data}')
    print(f'编码表: {code_table}')
    print(f'解码后的数据: {decoded_data}')