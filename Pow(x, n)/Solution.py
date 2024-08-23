class Solution(object):
    def myPow(self, x, n):

        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        def pow_recursive(x, n):
            if n == 0:
                return 1
            half = pow_recursive(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        return pow_recursive(x, n)
      
