citations = [3,0,6,1,5]         # Output: 3
citations = [1,3,1]             # Output: 1
citations = [1]                 # 1

for num in range(1,2):
    print(num)

import numpy as np

class Solution:
    def hIndex(self, citations) -> int:
        citations.sort(reverse=True)
        citations = np.array(citations)
        no_stop = 0
        for ind in range(len(citations)):   # ind=3
            if not sum((citations>=ind+1)*1)>=ind+1:
                no_stop = 1
                break
        return ind if no_stop == 1 else ind+1




