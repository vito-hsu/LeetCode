stones  = [0,1,3,5,6,8,12,17]
first   = stones[:len(stones)-1]
second  = stones[1:]
result1 = [stones[i+1]-stones[i] for i in stones if i < len(stones)-1]
result2 = [result1[i+1]-result1[i] for i in result1 if i < len(result1)-1]

class Solution:
    def canCross(self, stones):
        result1 = [stones[i+1]-stones[i] for i in stones if i < len(stones)-1]
        result2 = [result1[i+1]-result1[i] for i in result1 if i < len(result1)-1]
        if max(result2) >1 or min(result2)<-1:
            return False
        else:
            return True