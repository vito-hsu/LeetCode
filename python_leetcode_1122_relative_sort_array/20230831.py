arr1 = [2,3,1,3,2,4,6,7,9,2,19] ; arr2 = [2,1,4,3,9,6]           # Output: [2,2,2,1,4,3,3,9,6,7,19]

import collections

class Solution:
    def relativeSortArray(self, arr1, arr2):
        ans_list = []
        ans_list_tail = []
        key_dict = dict(collections.Counter(arr1).items())      # collections.Counter(arr1).most_common()
        for arr in arr2:            # arr = 2
            if arr in key_dict:
                ans_list += [arr]*key_dict[arr]

        key_set = set(arr2)
        for arr in arr1:
            if arr not in key_set:
                ans_list_tail.append(arr)
        ans_list_tail.sort()
        return ans_list+ans_list_tail