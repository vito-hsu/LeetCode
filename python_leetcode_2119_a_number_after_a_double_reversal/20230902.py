num = 1800      # Output: false

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        elif str(num)[-1]=='0':
            return False
        else:
            return True