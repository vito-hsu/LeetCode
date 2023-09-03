nums = [1,2,3,1]                # Output: true
nums = [1,1,1,3,3,4,3,2,4,2]    # Output: true
nums = [1,2,3,4]                # Output: false

from collections import Counter

class Solution:
    def containsDuplicate(self, nums) -> bool:
        if Counter(nums).most_common()[0][1]>1:
            return True
        else:
            return False
            