arr = [4,2,1,3]         # Output: [[1,2],[2,3],[3,4]]

import numpy as np

class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        arr1 = np.array(arr[1:])
        arr2 = np.array(arr[:-1])
        diffl = arr1-arr2
        min_value = min(diffl)
        indices = np.where(diffl==min_value)
        key_list1 = list(arr1[indices])
        key_list2 = list(arr2[indices])
        ans = list(zip(key_list2, key_list1))
        ans = [list(ele) for ele in ans]
        return ans


int(" ")
s = "4193 with words"
s[:5]