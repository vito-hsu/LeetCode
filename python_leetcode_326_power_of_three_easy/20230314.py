class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        key_list = [3**i for i in range(28)]
        if n<=0:
            return False
        elif n in key_list:
            return True
        else:
            return False