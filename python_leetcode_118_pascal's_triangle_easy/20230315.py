numRows = 25         # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

from numpy import array

def generate(numRows):        # numRows=3
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    else:
        key_list = []
        ans_list = generate(numRows-1)
        pre_list = ans_list[-1]
        key_list.extend(list(array(pre_list[:-1])+array(pre_list[1:])))
        key_list.insert(0, 1)
        key_list.insert(len(key_list),1)
        ans_list.append(key_list)
        return ans_list


class Solution:
    def generate(self, numRows):        # numRows=3
        return generate(numRows=numRows)
        
ans = Solution()
ans.generate(numRows=30)
