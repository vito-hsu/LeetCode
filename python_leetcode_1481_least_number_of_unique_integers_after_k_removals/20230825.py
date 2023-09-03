arr = [4,3,1,1,3,3,2] ; k = 3        # Output: 2

import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        key_list = [count for num,count in collections.Counter(arr).most_common()]
        key_list.sort()
        
        key_value = 0
        for ind, num in enumerate(key_list):        # ind = 0 ; num = key_list[0]
            key_value += num
            if key_value>k:
                return len(key_list)-ind
            elif key_value==k:
                return len(key_list)-ind-1