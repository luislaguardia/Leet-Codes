class Solution(object):
    def reverse(self, x: int) -> int:
  
        if x<0:
            sign =-1
            x=x*sign
        else:
            sign=1
        res = 0
        n=x
        while n!=0:
            rem = n%10
            res = res*10+rem
            n = n//10

        if -2**31<=res<=2**31 - 1:
            return res*sign
        else:
            return 0
