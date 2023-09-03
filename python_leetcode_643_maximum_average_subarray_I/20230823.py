nums = [1,12,-5,-6,50,3] ; k = 4    # Output: 12.75000
nums = [5] ; k = 1                  # Output: 5.00000


file_path = r"C:\Users\vito\Desktop\leetcode_0823.txt"  # 替换成实际的文件路径
with open(file_path, "r") as file:
    content = file.read()
nums = eval(content)
k = 7691



class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        ans_list = []
        start = sum(nums[:k])
        for i in range(1,len(nums)-k+1):  # i=1
            start = start-nums[0]
            nums.pop(0)
            start += nums[k-1]
            ans_list.append(start)            
        return max(ans_list)/k
    




class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        ans_list = []
        start = 9999999999
        for i in range(len(nums)-k+1):  # i=1
            print(i)
            if start != 9999999999:
                start = start-nums[0]
                nums.pop(0)
                start += nums[k-1]
                ans_list.append(start)
            else:
                start = sum(nums[:k])
                ans_list.append(start)
        return max(ans_list)/k
    


# import numpy as np

# class Solution:
#     def findMaxAverage(self, nums, k: int) -> float:
#         ans_list = []
#         for ind in range(len(nums)-k+1):
#             ans_list.append(nums[ind:(ind+k)])
#         row_mean = np.sum(np.array(ans_list), axis=1)
#         return max(row_mean)/k
