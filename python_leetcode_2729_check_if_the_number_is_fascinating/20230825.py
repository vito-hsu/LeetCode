
n = 192             # Output: true
n = 100             # Output: false
n = 267 
n = 783

class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n)+str(n*2)+str(n*3)
        if len(set(s))==9 and '0' not in s and len(s)==9:
            return True
        else:
            return False
