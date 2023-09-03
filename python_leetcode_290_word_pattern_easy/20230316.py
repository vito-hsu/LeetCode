pattern = "abba"    ;   s = "dog cat cat dog"   # Output: true
pattern = "abba"    ;   s = "dog cat cat fish"  # Output: false
pattern = "aaaa"    ;   s = "dog cat cat dog"   # Output: false

from numpy import unique

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res = [i + j for i, j in zip(list(pattern), list(s.split(" ")))]
        if len(list(pattern))==len(list(s.split(" "))) and len(unique(list(pattern))) == len(unique(list(s.split(" ")))) == len(unique(res)):
            return True
        else:
            return False
