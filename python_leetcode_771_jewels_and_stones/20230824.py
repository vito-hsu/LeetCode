jewels = "aA" ; stones = "aAAbbbb"  # Output: 3


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for jewel in jewels:
            # print(jewel)
            ans += stones.count(jewel)
        return ans