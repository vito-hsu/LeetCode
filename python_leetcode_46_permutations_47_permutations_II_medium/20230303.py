nums = [1,2,3]  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
nums = [1,1,2]


import itertools

class Solution:
    def permute(self, nums):
        return [list(item) for item in itertools.permutations(nums)]
    
###########################


import itertools

class Solution:
    def permuteUnique(self, nums):
        k = [list(item) for item in itertools.permutations(nums)]
        k.sort()                                                    # this line is very important if you want to use itertools.groupby()
        return list(i for i,_ in itertools.groupby(k))              # to delete the duplicates from a list of lists
    