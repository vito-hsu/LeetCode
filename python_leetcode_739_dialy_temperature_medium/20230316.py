temperatures = [73,74,75,71,69,72,76,73]    # Output: [1,1,4,2,1,1,0,0]
temperatures = [30,40,50,60]                # Output: [1,1,1,0]
temperatures = [30,60,90]                   # Output: [1,1,0]


import numpy as np

class Solution:
    def dailyTemperatures(self, temperatures):
        key_list = np.array(temperatures[1:].copy())
        ans_list = []
        for num in temperatures:            # num = temperatures[0]
            try:
                # ans_list.append(np.where(key_list>num)[0][0]+1)
                ans_list.append(next(x for x, val in enumerate(key_list) if val > num)+1)
            except:
                ans_list.append(0)
            finally:
                try:
                    key_list = np.delete(key_list, 0)
                except:
                    pass
        return ans_list