# py

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(remainder + ord('A')) + result  # Convert remainder to corresponding character and prepend it
            columnNumber //= 26  # Move to the next position
            
        return result
