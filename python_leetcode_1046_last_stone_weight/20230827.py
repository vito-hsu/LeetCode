stones = [2,7,4,1,8,1]      # Output: 1
stones = [1]                # Output: 1

class Solution:
    def lastStoneWeight(self, stones) -> int:
        for _ in range(len(stones)-1):
            stones = sorted(stones, reverse=True)
            key_num = stones[0]-stones[1]
            stones = stones[2:]
            stones.append(key_num)     
        return stones[0]       







