class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        dp = [0] * (n + 1)
        
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

test_cases = [2, 3, 5]
sol = Solution()
for n in test_cases:
    result = sol.climbStairs(n)
    print("Input: n =", n)
    print("Output:", result)
    print()
