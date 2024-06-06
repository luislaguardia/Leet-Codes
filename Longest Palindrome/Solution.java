class Solution {
public int longestPalindrome(String s) {
        Map<Character, Integer> counts = new HashMap();
        for (char c: s.toCharArray()) 
        counts.put(c, counts.getOrDefault(c, 0) + 1);

        int result = 0;
        boolean oddFound = false;
        for (int c: counts.values()) {
            if (c % 2 == 0) result += c;
            else {
                oddFound = true;
                result += c - 1;
            }
        }
        if (oddFound) result++;
        return result;
    }
}


// abccccdd
// a - 1
// b - 1
// c - 4
// d - 2
