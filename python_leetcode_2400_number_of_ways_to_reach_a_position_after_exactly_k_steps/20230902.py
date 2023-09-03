startPos = 1 ; endPos = 2 ; k = 3     # Output: 3
startPos = 1 ; endPos = 10 ; k = 3     # Output: 3
startPos = 1 ; endPos = 1000 ; k = 999 
startPos = 989 ; endPos = 1000 ; k = 99 

import math

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        key_num = (k-endPos+startPos)/2               # x + (x + end - start) = k
        if key_num<0:
            return 0

        if int(key_num) == key_num:
            if key_num==0:
                return 1            
            n = k
            get_num = int(key_num)
            return math.comb(n,get_num)%(10**9+7)
        else:
            return 0




# from itertools import permutations
# operators = ['+', '+', '-']
# permutations_list = list(permutations(operators))
# permutations_as_lists = [list(perm) for perm in permutations_list]
# for perm in permutations_as_lists:
#     print(perm)
