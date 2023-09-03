nums = [8,1,2,2,3]      # Output: [4,0,1,1,3]
nums = [7,7,7,7]        # Output: [0,0,0,0]



from scipy.stats import rankdata

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ranks = rankdata(nums, method='min')
        return list(ranks-1)










from scipy.stats import rankdata
data = [8, 1, 2, 2, 3]
ranks = rankdata(data, method='min')

print("元素的 rank:", ranks - 1)