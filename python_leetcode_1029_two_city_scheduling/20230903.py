costs = [[10,20],[30,200],[400,50],[30,20]]     # Output: 110
costs = [[10,10],[30,30],[400,400],[30,30]]


from scipy.stats import rankdata
from numpy import argsort

class Solution:
    def twoCitySchedCost(self, costs) -> int:
        key_list    = [abs(cost[0]-cost[1]) for cost in costs]
        rank        = rankdata(key_list)
        order       = argsort(rank)[::-1]
        ans_list    = []
        limit_0     = 0
        limit_1     = 0
        limit_num   = int(len(costs)/2)

        for ele in order:
            if costs[ele][0]<costs[ele][1] and limit_0!=limit_num:
                ans_list.append(costs[ele][0])
                limit_0 += 1
            elif costs[ele][0]>costs[ele][1] and limit_1!=limit_num:
                ans_list.append(costs[ele][1])
                limit_1 += 1
            elif limit_1==limit_num:
                ans_list.append(costs[ele][0])
                limit_0 += 1
            elif limit_0==limit_num:
                ans_list.append(costs[ele][1])
                limit_1 += 1
            elif costs[ele][0]==costs[ele][1]:
                ans_list.append(costs[ele][0])
                limit_0 += 1
            else:
                print("###################################################")
        return sum(ans_list)


# from scipy.stats import rankdata
# numbers = [10, 5, 8, 20, 3]
# rank = rankdata(numbers)
# print(rank)