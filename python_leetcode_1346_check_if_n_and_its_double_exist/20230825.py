arr = [10,2,5,3]        # Output: true    
arr = [3,1,7,11]        # Output: false
arr = [-20,8,-6,-14,0,-19,14,4]

import numpy as np

class Solution:
    def checkIfExist(self, arr) -> bool:
        ans = np.intersect1d(np.array(arr)*2, np.array(arr))
        if len(ans)>1 :
            return True
        elif len(ans)==1 and (arr.count(0)>1 or arr.count(0)==0):
            return True
        else:
            return False