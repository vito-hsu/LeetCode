nums = [1,2,3,3]            # Output: 3
nums = [5,1,5,2,5,3,5,4]    # Output: 5


import collections

class Solution:
    def repeatedNTimes(self, nums):
        key_num = int(len(nums)/2)
        key_tuple = collections.Counter(nums).most_common()  
        for ele in key_tuple:
            if ele[1]==key_num:
                return ele[0]