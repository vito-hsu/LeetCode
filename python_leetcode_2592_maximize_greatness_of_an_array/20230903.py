nums = [1,3,5,2,1,3,1]      # Output: 4
nums = [1,2,3,4]            # Output: 3
nums = [21]                 # Output: 0

with open(r"C:\Users\vito\Desktop\leetcode_0903.txt", 'r') as file:
    content = file.read()
nums = eval(content)



class Solution:
    def maximizeGreatness(self, nums) -> int:
        nums.sort()
        key_list = nums.copy()        
        ans = 0
        try:
            for num in nums:                        # num = 1
                if key_list[0]>num:
                    ans += 1
                    key_list.pop(0)
                else:
                    key_index = next((ind for ind, ele in enumerate(key_list) if ele>num), None)
                    key_list = key_list[key_index+1:]
                    ans += 1
        except:
            return ans

import time
start = time.time()
# for i in range(100000):
#     for j in range(1000):
#         ans = 1
#     ans = 0
a = Solution()
a.maximizeGreatness(nums=nums)
end = time.time()
end-start