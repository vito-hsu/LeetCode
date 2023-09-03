
k = int(2**31/2**4)

k = 1

len(''.join([str(i) for i in range(k*0*10**7, k*1*10**7)]))     # 68888890
len(''.join([str(i) for i in range(k*1*10**7, k*2*10**7)]))     # 80000000
len(''.join([str(i) for i in range(k*2*10**7, k*3*10**7)]))     # 80000000
len(''.join([str(i) for i in range(k*3*10**7, k*4*10**7)]))     # 80000000
len(''.join([str(i) for i in range(k*4*10**7, k*5*10**7)]))     # 80000000
len(''.join([str(i) for i in range(k*5*10**7, k*6*10**7)]))     # 80000000
len(''.join([str(i) for i in range(k*6*10**7, k*7*10**7)]))     # 80000000
len(''.join([str(i) for i in range(k*7*10**7, k*8*10**7)]))     # 80000000
len(''.join([str(i) for i in range(k*8*10**7, k*9*10**7)]))     # 80000000
len(''.join([str(i) for i in range(k*9*10**7, k*10*10**7)]))    # 80000000
len(''.join([str(i) for i in range(k*10*10**7, k*11*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*11*10**7, k*12*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*12*10**7, k*13*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*13*10**7, k*14*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*14*10**7, k*15*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*15*10**7, k*16*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*16*10**7, k*17*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*17*10**7, k*18*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*18*10**7, k*19*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*19*10**7, k*20*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*20*10**7, k*21*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*21*10**7, k*22*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*22*10**7, k*23*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*23*10**7, k*24*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*24*10**7, k*25*10**7)]))   # 90000000
len(''.join([str(i) for i in range(k*25*10**7, k*26*10**7)]))   # 90000000


a1 = 68888890
a2 = a1 + 80000000
a3 = a2 + 80000000
a4 = a3 + 80000000
a5 = a4 + 80000000
a6 = a5 + 80000000
a7 = a6 + 80000000
a8 = a7 + 80000000
a9 = a8 + 80000000
a10 = a9 + 80000000
a11 = a10 + 90000000
a12 = a11 + 90000000
a13 = a12 + 90000000
a14 = a13 + 90000000
a15 = a14 + 90000000
a16 = a15 + 90000000
a17 = a16 + 90000000
a18 = a17 + 90000000
a19 = a18 + 90000000
a20 = a19 + 90000000
a21 = a20 + 90000000
a22 = a21 + 90000000
a23 = a22 + 90000000
a24 = a23 + 90000000
a25 = a24 + 90000000
a26 = a25 + 90000000
key = 1

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <10:
            return n
        elif n == 10:
            return 1
        elif n == 11:
            return 0
        elif n <= a1:
            a = [str(i) for i in range(key*0*10**7, key*1*10**7)]
            return int(''.join(a)[n])            
        elif n <= a2:
            a = [str(i) for i in range(key*1*10**7, key*2*10**7)]
            n = n - a1
            return int(''.join(a)[n])        
        elif n <= a3:
            a = [str(i) for i in range(key*2*10**7, key*3*10**7)]
            n = n - a2
            return int(''.join(a)[n])       
        elif n <= a4:
            a = [str(i) for i in range(key*3*10**7, key*4*10**7)]
            n = n - a3
            return int(''.join(a)[n])                  
        elif n <= a5:
            a = [str(i) for i in range(key*4*10**7, key*5*10**7)]
            n = n - a4
            return int(''.join(a)[n])                  
        elif n <= a6:
            a = [str(i) for i in range(key*5*10**7, key*6*10**7)]
            n = n - a5
            return int(''.join(a)[n])  
        elif n <= a7:
            a = [str(i) for i in range(key*6*10**7, key*7*10**7)]
            n = n - a6
            return int(''.join(a)[n])  
        elif n <= a8:
            a = [str(i) for i in range(key*7*10**7, key*8*10**7)]
            n = n - a7
            return int(''.join(a)[n])  
        elif n <= a9:
            a = [str(i) for i in range(key*8*10**7, key*9*10**7)]
            n = n - a8
            return int(''.join(a)[n])  
        elif n <= a10:
            a = [str(i) for i in range(key*9*10**7, key*10*10**7)]
            n = n - a9
            return int(''.join(a)[n])  
        elif n <= a11:
            a = [str(i) for i in range(key*10*10**7, key*11*10**7)]
            n = n - a10
            return int(''.join(a)[n])  
        elif n <= a12:
            a = [str(i) for i in range(key*11*10**7, key*12*10**7)]
            n = n - a11
            return int(''.join(a)[n])  
        elif n <= a13:
            a = [str(i) for i in range(key*12*10**7, key*13*10**7)]
            n = n - a12
            return int(''.join(a)[n])  
        elif n <= a14:
            a = [str(i) for i in range(key*13*10**7, key*14*10**7)]
            n = n - a13
            return int(''.join(a)[n])  
        elif n <= a15:
            a = [str(i) for i in range(key*14*10**7, key*15*10**7)]
            n = n - a14
            return int(''.join(a)[n])  
        elif n <= a16:
            a = [str(i) for i in range(key*15*10**7, key*16*10**7)]
            n = n - a15
            return int(''.join(a)[n])  
        elif n <= a17:
            a = [str(i) for i in range(key*16*10**7, key*17*10**7)]
            n = n - a16
            return int(''.join(a)[n])  
        elif n <= a18:
            a = [str(i) for i in range(key*17*10**7, key*18*10**7)]
            n = n - a17
            return int(''.join(a)[n])  
        elif n <= a19:
            a = [str(i) for i in range(key*18*10**7, key*19*10**7)]
            n = n - a18
            return int(''.join(a)[n])  
        elif n <= a20:
            a = [str(i) for i in range(key*19*10**7, key*20*10**7)]
            n = n - a19
            return int(''.join(a)[n])  
        elif n <= a21:
            a = [str(i) for i in range(key*20*10**7, key*21*10**7)]
            n = n - a20
            return int(''.join(a)[n])  
        elif n <= a22:
            a = [str(i) for i in range(key*21*10**7, key*22*10**7)]
            n = n - a21
            return int(''.join(a)[n])  
        elif n <= a23:
            a = [str(i) for i in range(key*22*10**7, key*23*10**7)]
            n = n - a22
            return int(''.join(a)[n])  
        elif n <= a24:
            a = [str(i) for i in range(key*23*10**7, key*24*10**7)]
            n = n - a23
            return int(''.join(a)[n])  
        elif n <= a25:
            a = [str(i) for i in range(key*24*10**7, key*25*10**7)]
            n = n - a24
            return int(''.join(a)[n])  
        else:
            a = [str(i) for i in range(key*25*10**7, key*26*10**7)]
            n = n - a25
            return int(''.join(a)[n])
    
    
ans = Solution()
ans.findNthDigit(n=160000001)        

int(''.join([str(i) for i in range(160000001)])[160000001])





##################
matrix = [[1,2,3],[4,5,6],[7,8,9]]

import numpy as np
m = np.array([[1,2,3],
         [2,3,3],
         [5,4,3]])
class Solution:
    def rotate(self, matrix):
        return np.rot90(matrix, axes=(1, 0)).tolist()

ans = Solution()
ans.rotate(matrix=matrix)


##################

n=1999
ans = 4

class Solution:
    def isHappy(self, n):
        j       = 0
        first   = 0
        second  = 0
        third   = 0
        fourth  = 0
        fifth   = 0
        ans     = n
        while ans!=1:
            if (ans == first or ans == second or ans == third or ans == fourth or ans == fifth or ans == 4) and j>5:
                break            
            ans     = sum([int(i)**2 for i in str(ans)])
            print(ans)
            if j == 0:
                first = ans
            if j == 1:
                second = ans
            if j == 2:
                third = ans
            if j == 3:
                fourth = ans
            if j == 4:
                fifth = ans
            j+=1


        if ans == 1:
            return True
        else:
            return False
        
ans = Solution()
ans.isHappy(n=n)