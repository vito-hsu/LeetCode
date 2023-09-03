candidates = [2,3,6,7]  ;   target = 7  # Output: [[2,2,3],[7]]
candidates = [2,3,5]    ;   target = 8  # Output: [[2,2,2,2],[2,3,3],[3,5]]


candidates  = [8,10,9,32,25,27,22,38,15,5,3,26,30,11,21,36,37]
target      = 39


candidates  = [5]
target      = 12


candidates  = [38]
target      = 35


candidates  = [2,22,4,17,28,13,39,27,24,37,12,30,5,23,29,8,16,34,15,36,14,10,31]
target      = 30


import itertools

class Solution:
    def combinationSum(self, candidates, target):
        iters       = round(target*min(candidates)**(-1)) 
        ans_list    = []
        candidates.sort()
        for num in candidates:
            if min(candidates)+num > target and num != target:
                candidates.remove(num)
        if candidates == []:
            return []
        for iter in range(iters, 0, -1):        # iter = 3
            if iter == iters and target % iters ==0 and target % min(candidates) ==0:
                ans_list.append([min(candidates) for _ in range(iters)])
                continue
            # the following four lines are the most important key in this question !!!!
            candidates_we_need = candidates.copy()
            for index,j in enumerate(candidates):
                if j>target-(iter-1)*min(candidates):
                    candidates_we_need = candidates_we_need[:index+1]
                    break
            print("candidates_we_need", candidates_we_need)
            for seq in itertools.combinations_with_replacement(candidates_we_need, iter):
                if sum(seq) == target:
                    ans_list.append(list(seq))
                    print(seq)
        return ans_list#[list(seq) for i in range(0, iters+1) for seq in itertools.combinations_with_replacement(candidates, i) if sum(seq)==target]

ans = Solution()
ans.combinationSum(candidates=candidates, target=target)





###########################




candidates = [10,1,2,7,6,1,5]   ;   target = 8  # Output [[1,1,6],[1,2,5],[1,7],[2,6]]


candidates  = [14,18,19,30,6,5,14,23,28,18,26,21,12,15,29,18,32,23,6,21,19,30,6,28,17,13,29,28,10,34,26,11,10,32,7,11,32,8,21,18,22,5,34,21,7,20,26,5,9,28,21,23,23,15,8,27,23,32,12,20,31,33,27,28,30,21,34,19]
target      = 29

candidates  = [5,24,28,14,13,28,12,29,22,8,16,28,11,5,8,20,10,27,16,19,16,15,14,14,9,23,30,13,33,24,24,33,14,18,5,14,33,12,30,21,15,12,14,13,34,9,20,9,31,32,16]
target      = 29

candidates  = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target      = 30

candidates  = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target      = 30




import itertools



class Solution:
    def combinationSum2(self, candidates, target):
        iters       = round(target*min(candidates)**(-1)) 

        for num in set(candidates):
            while candidates.count(num)>target:
                candidates.remove(num)
        candidates.sort()

        for num in candidates:
            if min(candidates)+num > target and num != target:
                candidates.remove(num)        
        ans_list = []
        print("len(candidates):",len(candidates))
        for iter in range(iters, 0, -1):                            # iter =30
            if sum(candidates[len(candidates)-iter:])<target:
                continue
            candidates_we_need = candidates.copy()
            for index,j in enumerate(candidates):
                if j>target-(iter-1)*min(candidates):
                    candidates_we_need = candidates_we_need[:index+1]
                    break
            for seq in itertools.combinations(candidates_we_need, iter):
                if sum(seq)==target:
                    seq = list(seq)
                    ans_list.append(seq)
                    # print(seq)
        ans_list.sort()                                                    # this line is very important if you want to use itertools.groupby()
        return list(i for i,_ in itertools.groupby(ans_list)) 
    

ans = Solution()
ans.combinationSum2(candidates=candidates, target=target)