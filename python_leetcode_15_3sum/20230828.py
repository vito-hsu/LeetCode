nums = [-1,0,1,2,-1,-4]|             # Output: [[-1,-1,2],[-1,0,1]]
nums = [0,1,1]                      # Output: []
nums = [0,0,0]                      # Output: [[0,0,0]]

with open(r"C:\Users\vito\Desktop\leetcode_0828-2.txt", 'r') as file:
    content = file.read()
nums = eval(content)


from time import time

class Solution:
    def threeSum(self, nums):
        # start = time()

        ans_list = []
        key_list1 = nums.copy()
        key_list2 = nums.copy()
        key_list1.sort()
        key_list2.sort(reverse=True)
        key_set = set(nums)
        for num in key_list1:
            if num<0:
                continue
            for num2 in key_list2:
                if num2>0:
                    continue
                if 0-num-num2 in key_set:
                    ans_list.append([num, 0-num-num2, num2])

        return ans_list
        # end = time()
        # end-start
























# class Solution:
#     def threeSum(self, nums):
#         ans_list = []
#         nums.sort()
#         for ind, num in enumerate(nums):            # ind = 1 ; num = nums[1]
#             print(ind)                              
#             if num>0:                               # key1
#                 continue
#             max_value   = nums[-1]
#             min_value   = nums[ind+1]
#             key_index1  = next((i+ind for i, ele in enumerate(nums[ind+1:]) if ele > num+max_value), None)
#             key_index2  = next((i+ind for i, ele in enumerate(nums[ind+1:]) if num+min_value < -1*(ele)), None)
#             if key_index1== None or key_index2==None:
#                 continue
#             key_list    = nums[key_index1:]
#             for ind2, num2 in enumerate(key_list):
#                 if num+num2>0:                      # key2
#                     break
#                 key_set = set(key_list[ind2+1:])
#                 if 0-num-num2 in key_set:
#                     ans = [num, num2, 0-num-num2]
#                     ans.sort()
#                     ans_list.append(ans)
#         ans_list = list(set([tuple(l) for l in ans_list]))
#         return [list(l) for l in ans_list]
    







