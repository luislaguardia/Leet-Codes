class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        count = 0
        operations = 0
        for i in range(n):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count

        count = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count
        
        return answer
