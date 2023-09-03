n = 2       # Output: 1
n = 4       # Output: 3


def fib1(n):
    if n==0:
        return 0
    
    if n==1:
        return 1
    
    if n>=2:
        return fib1(n-1)+fib1(n-2)

class Solution:
    def fib(self, n: int) -> int:
        return fib1(n)