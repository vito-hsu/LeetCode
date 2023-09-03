n = 6   # Output: true
n = 1   # Output: true
n = 14  # Output: false
n = 9091
n = 8


class Solution:
    def isUgly(self, n):
        if n<=0:
            return False
        while n%2==0 or n%3==0 or n%5==0 or n ==1:
            if n == 1:
                return True
            if n%2==0:
                n = n//2
            if n%3==0:
                n = n//3
            if n%5==0:
                n = n//5
        return False



ans = Solution()
ans.isUgly(n=n)



##################################
n = 10      # Output: 12
n = 1       # Output: 1
n = 700     # 5898240
n = 1300    # 306110016

import numpy as np
from itertools import product
from math import prod

key_list1 = [2**j for j in range(40)]
key_list2 = [3**j for j in range(35)]
key_list3 = [5**j for j in range(30)]
key_list4 = [key_list1, key_list2, key_list3]
len([list(i) for i in product(*key_list4)])
key = [prod(list(i)) for i in product(*key_list4)]
key.sort()
key[:1000]
len(key)
key = key[:1690]

class Solution:
    def nthUglyNumber(self, n):
        return key[n-1]