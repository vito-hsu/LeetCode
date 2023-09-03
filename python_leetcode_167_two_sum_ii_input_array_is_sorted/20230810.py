numbers = [2,7,11,15] ; target = 9  # [1,2]
numbers = [-1,0] ; target = -1      # [1,2]


import numpy as np

class Solution:
    def twoSum(self, numbers, target: int):
        numbers = np.array(numbers)
        numbers = numbers[numbers<=target] if target>0 else numbers
        numbers = numbers[numbers>=target] if target<0 else numbers
        for ind, num in enumerate(numbers):
            if target-num in numbers:
                ans1 = ind+1
                ans2 = np.where(numbers == target-num)[0][0]+1
                return [ans1, ans2] if ans1!=ans2 else [ans1, ans2+1]
            


numbers = np.array(numbers)
numbers = numbers[numbers<=target] if target>0 else numbers[numbers>=target]
for ind, num in enumerate(numbers):
    if target-num in numbers:
        print([ind+1, np.where(numbers == target-num)[0][0]+1])