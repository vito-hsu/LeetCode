nums = [1,3,-1,-3,5,3,6,7]  ;   k = 3   # Output: [3,3,5,5,6,7]

import pandas as pd


class Solution:
    def maxSlidingWindow(self, nums, k):
        data = {'nums':nums}
        df = pd.DataFrame(data=data)
        return [int(x) for x in list(df['nums'].rolling(window=k).max()[k-1:])]
    

########################

import itertools

class Solution:
    def maxSlidingWindow(self, nums, k):
        it = iter(nums)
        for element in it:
            yield [i for i in itertools.islice(nums,k,1)]

ans = Solution()
ans.maxSlidingWindow(nums=nums, k=k)
        # ans_list = []
        # start = 0
        # end = k
        # for _ in range(0, len(nums)-k+1):
        #     ans_list.append(max(nums[start:end]))
        #     start+=1
        #     end+=1
        # return ans_list