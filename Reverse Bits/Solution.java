public class Solution {
    private final int[] lookup = new int[256];

    public Solution() {
        for (int i = 0; i < 256; i++) {
            lookup[i] = reverse8Bits(i);
        }
    }

    private int reverse8Bits(int n) {
        int result = 0;
        for (int i = 0; i < 8; i++) {
            result <<= 1;
            result |= (n & 1);
            n >>= 1;
        }
        return result;
    }

    public int reverseBits(int n) {
        return (lookup[n & 0xFF] << 24) |
               (lookup[(n >>> 8) & 0xFF] << 16) |
               (lookup[(n >>> 16) & 0xFF] << 8) |
               lookup[(n >>> 24) & 0xFF];
    }
}
