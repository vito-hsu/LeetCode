n = 2               # Output: [0,1,1]
n = 5               # Output: [0,1,1,2,1,2]



class Solution:
    def countBits(self, n: int):
        ans_list = []

        for num in range(n+1):        # num=0
            ans = 0
            for num2 in bin(num)[2:]:
                ans += int(num2)
            ans_list.append(ans)

        return ans_list