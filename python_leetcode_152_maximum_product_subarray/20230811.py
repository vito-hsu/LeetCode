nums = [2,3,-2,4]                           # 6
nums = [-2,0,-1]                            # 0
nums = [2,3,-2,4,-7,-10]                    # 336
nums = [2,3,-2,4,-7,-10,1,-1000]            # 10000
nums = [2,3,-2,4,-7,-10,1,0,-1000]          # 336
nums = [2,3,-2,4,-7,0,-10,1,0,-1000]        # 336




# import numpy as np

# def array_split_by_zero(nums):
#     arr             = np.array(nums)
#     zero_indices    = np.where(arr == 0)[0]                                                     # Find the indices where the array equals 0
#     segments        = np.split(arr, zero_indices)                                               # Split the array into segments based on zero indices
#     segments        = [segment[1:] if segment[0] == 0 else segment for segment in segments]     # Remove leading zeros from each segment
#     segments        = [segment for segment in segments if len(segment) > 0]                     # Remove empty segments
#     return segments



# def key_calculate(segment):
#     key_list = []

    
# class Solution:
#     def maxProduct(self, nums) -> int:
#         nums        = array_split_by_zero(nums=nums)
#         key_list    = []
#         for segment in nums:




def max_subarray_product(nums):
    n = len(nums)
    if n == 0:
        return 0
    max_product = min_product = result = nums[0]
    for i in range(1, n):           # i=2
        num = nums[i]
        if num < 0:
            max_product, min_product = min_product, max_product
        max_product = max(num, num * max_product)
        min_product = min(num, num * min_product)
        result = max(result, max_product)
    return result


sublist = [2,3,-2,4,-7,0,-10,1,0,-1000]
max_subarray_product(sublist)