n = 8           # Output: 6

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return -1

        key_list = [num for num in range(1, n+1)]
        for ind in range(1, n):           # ind = 6
            # print(key_list[:ind], key_list[ind+1:])
            if sum(key_list[:ind])==sum(key_list[ind+1:]):
                # print(ind+1)
                return ind+1
        return -1