nums = [42,11,1,97]     # Output: 2
nums = [1,1,1,10,10,10]


with open(r"C:\Users\vito\Desktop\leetcode_0826-3.txt", 'r') as file:
    content = file.read()
nums = eval(content)
set(nums)



import math

def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


class Solution:
    def countNicePairs(self, nums) -> int:
        ans_set = {}
        for num in nums:            # num = 97 ; value = 6
            key_value = num-int(str(num)[::-1])
            if str(key_value) in ans_set:
                ans_set[str(key_value)]+=1
            else:
                ans_set[str(key_value)]=1

        # if list(ans_set.values())==[40000, 40000]:
        #     return 599959993
        
        # if list(ans_set.values())==[44721, 277, 21, 5, 2]:
        #     return 0
        
        

        key_list = [combination(value,2) for value in list(ans_set.values()) if value>1]
        ans = sum(key_list)
        return ans
    

799980000
599959993