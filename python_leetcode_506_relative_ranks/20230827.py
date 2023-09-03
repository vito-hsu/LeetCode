score = [10,3,8,9,4]            # Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
score = [10] 


import scipy.stats

class Solution:
    def findRelativeRanks(self, score):
        rank_data   = scipy.stats.rankdata(score, method='average')
        ans_list    = [str(int(len(score)+1-num)) for num in rank_data]
        try:
            ans_list[ans_list.index('1')]='Gold Medal'
            ans_list[ans_list.index('2')]='Silver Medal'
            ans_list[ans_list.index('3')]='Bronze Medal'
        except:
            pass
        return ans_list












import scipy.stats

data = [10, 3, 8, 9, 4]
rank = scipy.stats.rankdata(data, method='average')
print(rank)  # 输出 [5.0, 1.0, 3.0, 4.0, 2.0]
[int(len(data)+1-num) for num in rank]