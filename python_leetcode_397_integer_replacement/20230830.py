n = 8           # Output: 3
n = 7           # Output: 4
n = 122
n = 859
n = 445421
n = 3

def two_factors(n):
    ans = 0
    while n%2==0:
        n = n/2
        ans += 1
    return ans

class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n!=1:
            if n==3:
                return ans+2
            elif n==11:
                return ans+5

            if int(n/2)-n/2!=0:
                key_num1 = two_factors(n+1)
                key_num2 = two_factors(n-1)
                if key_num1>key_num2:
                    n = int((n+1)/2)
                    ans += 2
                else:
                    n = int((n-1)/2)
                    ans += 2
            else:
                n = int(n/2)
                ans += 1


        return ans