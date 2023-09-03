x = 121             # Output: true
x = -121            # Output: false
x = 10              # Output: false

class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            if int(str(x)[::-1])==x:
                return True
            else:
                return False
        except:
            return False