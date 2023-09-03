prices = [7,1,5,3,6,4]  # Output: 5

from numpy import array

class Solution:
    def maxProfit(self, prices) -> int:
        key_list = [max(prices[i+1:]) for i in range(len(prices)-1)]
        key_ans  = array(key_list) - array(prices[:-1])


##################
matrix = [[1,5,9],[10,11,13],[12,13,15]]    ;   k = 8       # Output: 13
matrix = [[-5]]                             ;   k = 1       # Output: -5
matrix = [[1,2],[1,3]]                      ;   k = 2       # Output: 1


import numpy as np

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        key_list = np.matrix(matrix).flatten().tolist()[0]
        key_list.sort()
        return key_list[k-1]


##################
nums = [1,3,4,2,2]  # Output: 2
nums = [3,1,3,4,2]  # Output: 3

from collections import Counter

class Solution:
    def findDuplicate(self, nums) -> int:
        return Counter(nums).most_common()[0][0]



##################
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        key_value = ''
        for i in range(1,n+1):
            key_value+=str(i)
        ans = ''
        for i in list(permutations(key_value))[k-1]:
            ans+=i
        return ans