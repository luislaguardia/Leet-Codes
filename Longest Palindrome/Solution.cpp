#include <unordered_map>
#include <string>

class Solution {
public:
    int longestPalindrome(std::string s) {
        std::unordered_map<char, int> counts;
        for (char c : s) counts[c]++;

        int result = 0;
        bool oddFound = false;
        for (auto& pair : counts) {
            if (pair.second % 2 == 0) {
                result += pair.second;
            } else {
                oddFound = true;
                result += pair.second - 1;
            }
        }
        if (oddFound) {
            result++;
        }
        return result;
    }
};
