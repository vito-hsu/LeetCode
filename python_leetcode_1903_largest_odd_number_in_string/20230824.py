num = "52"  # Output: "5"

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for ind, re_num in enumerate(num[::-1]):        # ind = 0 ; re_num = '2'
            print(ind)
            if int(re_num)%2==1:
                return num[:len(num)-ind]
        return ""
            
ans = Solution()
ans.largestOddNumber(num=num)