import argparse
import hashlib  # hashlib 只在 Test 类中使用
import struct
import unittest


class SHA1Hash:
    """
    整个 SHA1 哈希算法的管道类
    """

    def __init__(self, data):
        """
        初始化变量 data 和 h。h 是一个包含 5 个 8 位十六进制数字的列表，分别对应 (1732584193, 4023233417, 2562383102, 271733878, 3285377520)。我们将这作为消息摘要的初始值。在 Python 中，使用 0x 来表示十六进制数字
        """
        self.data = data
        self.h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

    @staticmethod
    def rotate(n, b):
        """
        用于其他方法内部的静态方法。左旋转 n，位移 b 位。
        """
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    def padding(self):
        """
        将输入消息用零填充，以使填充后的数据长度为 64 字节或 512 位
        """
        padding = b"\x80" + b"\x00" * (63 - (len(self.data) + 8) % 64)
        padded_data = self.data + padding + struct.pack(">Q", 8 * len(self.data))
        return padded_data

    def split_blocks(self):
        """
        返回一个列表，其中包含长度为 64 的字节字符串
        """
        return [
            self.padded_data[i : i + 64] for i in range(0, len(self.padded_data), 64)
        ]

    # @staticmethod
    def expand_block(self, block):
        """
        接受长度为 64 的字节字符串块，将其解压为整数列表，并返回一组经过一些位运算后的 80 个整数
        """
        w = list(struct.unpack(">16L", block)) + [0] * 64
        for i in range(16, 80):
            w[i] = self.rotate((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        return w

    def final_hash(self):
        """
        调用所有其他方法来处理输入数据。填充数据，然后分割为块，然后对每个块进行一系列操作（包括扩展）。对于每个块，初始化的变量 h 被复制到 a、b、c、d、e 这 5 个变量中，然后这 5 个变量经历了几次更改。处理完所有块后，这 5 个变量被两两相加，即将 a 添加到 h[0]，b 添加到 h[1]，依此类推。这个 h 就是我们的最终哈希值，返回它。
        """
        self.padded_data = self.padding()
        self.blocks = self.split_blocks()
        for block in self.blocks:
            expanded_block = self.expand_block(block)
            a, b, c, d, e = self.h
            for i in range(0, 80):
                if 0 <= i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                a, b, c, d, e = (
                    self.rotate(a, 5) + f + e + k + expanded_block[i] & 0xFFFFFFFF,
                    a,
                    self.rotate(b, 30),
                    c,
                    d,
                )
        self.h = (
            self.h[0] + a & 0xFFFFFFFF,
            self.h[1] + b & 0xFFFFFFFF,
            self.h[2] + c & 0xFFFFFFFF,
            self.h[3] + d & 0xFFFFFFFF,
            self.h[4] + e & 0xFFFFFFFF,
        )
        return "%08x%08x%08x%08x%08x" % tuple(self.h)


class SHA1HashTest(unittest.TestCase):
    """
    SHA1Hash 类的测试类。继承自 unittest 的 TestCase 类
    """

    def testMatchHashes(self):
        msg = bytes("Test String", "utf-8")
        self.assertEqual(SHA1Hash(msg).final_hash(), hashlib.sha1(msg).hexdigest())


def main():
    """
    提供选项 'string' 或 'file' 来接收输入，并打印计算得到的 SHA1 哈希值。
    unittest.main() 已被注释，因为我们可能不希望每次都运行测试。
    """
    # unittest.main()
    parser = argparse.ArgumentParser(description="Process some strings or files")
    parser.add_argument(
        "--string",
        dest="input_string",
        default="Hello World!! Welcome to Cryptography",
        help="Hash the string",
    )
    parser.add_argument("--file", dest="input_file", help="Hash contents of a file")
    args = parser.parse_args()
    input_string = args.input_string
    # 无论如何哈希输入都应该是一个字节字符串
    if args.input_file:
        hash_input = open(args.input_file, "rb").read()
    else:
        hash_input = bytes(input_string, "utf-8")
    print(SHA1Hash(hash_input).final_hash())


if __name__ == "__main__":
    main()
