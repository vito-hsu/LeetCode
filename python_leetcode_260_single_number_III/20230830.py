nums = [1,2,1,3,2,5]        # Output: [3,5]

import collections

class Solution:
    def singleNumber(self, nums):
        ans = collections.Counter(nums).most_common()[::-1][:2]
        return [num for num,count in ans]
        