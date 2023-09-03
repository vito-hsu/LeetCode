n = 27


import itertools

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        numbers     = [3**num for num in range(15)]
        numbers     = [num for num in numbers if num<=n]
        ans_list    = []
        for r in range(len(numbers) + 1):
            combs = itertools.combinations(numbers, r)
            for comb in combs:
                total = sum(comb)
                ans_list.append(total)
        
        ans_list = set(ans_list)        # len(ans_list)
        if n in ans_list:
            return True
        else:
            return False
        


# numbers     = [1,3,5]
# for r in range(len(numbers) + 1):
#     combs = itertools.combinations(numbers, r)
#     for comb in combs:
#         print(comb) ;   total = sum(comb)  ;  print(total)