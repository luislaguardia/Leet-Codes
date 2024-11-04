class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to make it 0-based
            remainder = columnNumber % 26
            result = chr(remainder + ord('A')) + result  # Convert remainder to corresponding character and prepend it
            columnNumber //= 26  # Move to the next position
            
        return result
