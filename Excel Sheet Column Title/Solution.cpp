class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result;
        
        while (columnNumber > 0) {
            columnNumber--;
            int remainder = columnNumber % 26;
            result += ('A' + remainder);
            columnNumber /= 26;
        }
        
        reverse(result.begin(), result.end());  // Reverse the result as we build it backwards
        return result;
    }
};