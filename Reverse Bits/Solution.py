class Solution:
    def __init__(self):
        self.lookup = [0] * 256
        for i in range(256):
            self.lookup[i] = self.reverse8Bits(i)

    def reverse8Bits(self, n):
        result = 0
        for i in range(8):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
    
    def reverseBits(self, n: int) -> int:
        return (self.lookup[n & 0xFF] << 24) | \
               (self.lookup[(n >> 8) & 0xFF] << 16) | \
               (self.lookup[(n >> 16) & 0xFF] << 8) | \
               self.lookup[(n >> 24) & 0xFF]
