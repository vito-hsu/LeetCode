c = 5   # Output: true


import numpy as np

key_set = set(np.array([num for num in range(46341)])**2)       # len(key_set)

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for num in list(key_set):
            if c-num in key_set:
                return True
            
            