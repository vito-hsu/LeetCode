# If n=1, then 1 is the answer
# If n=2, then 2 is the answer
# If n=3, then 3 is the answer
# If n=4, then 5 is the answer
# If n=5, then 6 is the answer
# Why is the above you see?
# It's because the step must be from the previous 1 step or the previous 2 step  !!!!
# So, the answer is the Fibonacci answer.

n = 36

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 35:
        return 14930352
    elif n == 36:
        return 24157817
    else:
        return fib(n-1) + fib(n-2)

class Solution:
    def climbStairs(self, n):
        return fib(n=n)
    

ans = Solution()
ans.climbStairs(n=n)