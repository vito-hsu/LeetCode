n = 1       # Output: true


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        key_list = [2**i for i in range(32)]
        if n<=0:
            return False
        elif n in key_list:
            return True
        else:
            return False
        
#######################


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        key_list = [4**i for i in range(16)]
        if n<=0:
            return False
        elif n in key_list:
            return True
        else:
            return False        

[i**2 for i in range(1,101)]

########################

10//3
7//-3
0//-3
1//-3
1%3
dividend = 10   ;   divisor = 3     # Output: 3
dividend = 7    ;   divisor = -3    # Output: -2

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend%divisor!=0 and divisor*dividend<0:
            ans = dividend//divisor+1
        else:
            ans = dividend//divisor
        
        if ans>2**31-1:
            ans = 2**31-1
        elif ans<-2**31:
            ans = -2**31
        return ans