patterns = ["a","abc","bc","d"] ; word = "abc"   # Output: 3
patterns = ["a","b","c"] ; word = "aaaaabbbbb"   # Output: 2
patterns = ["a","a","a"] ; word = "ab"           # Output: 3



class Solution:
    def numOfStrings(self, patterns, word: str) -> int:
        ans = 0
        for pattern in patterns:    # pattern = patterns[0]
            if pattern in word:
                ans+=1
        return ans










