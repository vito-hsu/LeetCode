s = "aaabbbcc"      # Output: 2
s = "aab"           # Output: 0
s = "ceabaacb"      # Output: 2
s = "abcabc"        # Output: 3
s = "bbcebab"       # 

import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        key_list = [count for num,count in collections.Counter(s).most_common()]
        ans = 0
        for ind, num in enumerate(key_list):            # num = 1  ; ind = 2
            if key_list.count(num)>1:
                key_value = max(set(range(num))-set(key_list)) if len(set(range(num))-set(key_list))>0 else 0
                ans += num - key_value
                key_list[ind] = key_value
        return ans