prices = [7,1,5,3,6,4]      # Output: 5
prices = [7,6,4,3,1]        # Output: 0


import numpy as np

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices)==1:
            return 0
        else:
            key_list = [0]
            key_value = prices[-1]
            for i in range(len(prices)-2,-1,-1):
                if prices[i]<key_value:
                    key_list.append(key_value)
                else:
                    key_list.append(prices[i])
                    key_value = prices[i]
            key_list.reverse()
            return max(np.array(key_list)-np.array(prices))
        

