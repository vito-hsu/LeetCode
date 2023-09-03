num = 16            # Output: true
num = 14            # Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num**0.5-int(num**0.5)==0:
            return True
        else:
            return False