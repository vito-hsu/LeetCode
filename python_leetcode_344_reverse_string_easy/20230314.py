s = ["h","e","l","l","o"]       # Output: ["o","l","l","e","h"]
s = ["H","a","n","n","a","h"]   # Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s) -> None:
        s.reverse()
        