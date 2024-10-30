#include <string>
#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        string cleaned;

        for (char c : s) {
            if (isalnum(c)) {
                cleaned += tolower(c);
            }
        }

        int left = 0;
        int right = cleaned.length() - 1;
        
        while (left < right) {
            if (cleaned[left] != cleaned[right]) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
};
