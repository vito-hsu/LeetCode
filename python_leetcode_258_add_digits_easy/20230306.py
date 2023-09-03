num = 38    # output: 2

class Solution:
    def addDigits(self, num):
        ans = num
        j = 0
        while ans>9 or j==0:
            ans = sum([int(i) for i in str(ans)])
            j = j+1
        return ans
    

ans = Solution()
ans.addDigits(num=num)