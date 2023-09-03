n = 12 ; k = 3       # Output: 3

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = 0
        for num in range(1,n+1):
            if n%num==0:
                ans += 1
                if ans == k:
                    return num
        return -1