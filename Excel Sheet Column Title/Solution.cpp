class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result;
        
        while (columnNumber > 0) {
            columnNumber--;  // Adjust to make it 0-based
            int remainder = columnNumber % 26;
            result += ('A' + remainder);  // Convert remainder to corresponding character
            columnNumber /= 26;  // Move to the next position
        }
        
        reverse(result.begin(), result.end());  // Reverse the result as we build it backwards
        return result;
    }
};
