n = 10          # Output: 4
n = 6500000

# class Solution:
#     def countPrimes(self, n):
#         if n<=2:
#             return 0
#         elif n<=3:
#             return 1
#         elif n<=5:
#             return 2    
#         elif n<=7:
#             return 3
#         elif n<=11:
#             return 4
#         elif n<=13:
#             return 5
#         elif n<=17:
#             return 6
#         elif n<=19:
#             return 7
#         elif n<=23:
#             return 8
#         elif n<=29:
#             return 9
#         elif n<=31:
#             return 10
#         elif n<=37:
#             return 11
#         elif n<=41:
#             return 12
#         elif n<=43:
#             return 13
#         elif n<=47:
#             return 14
#         elif n<=53:
#             return 15
#         elif n<=59:
#             return 16
#         elif n<=61:
#             return 17
#         elif n<=67:
#             return 18
#         elif n<=71:
#             return 19
#         elif n<=73:
#             return 20
#         elif n<=79:
#             return 21
#         elif n<=83:
#             return 22
#         elif n<=89:
#             return 23
#         elif n<=97:
#             return 24
#         elif n<=101:
#             return 25
#         elif n<=103:
#             return 26
#         elif n<=107:
#             return 27
#         elif n<=109:
#             return 28
#         elif n<=113:
#             return 29
#         elif n<=127:
#             return 30
#         elif n<=131:
#             return 31
#         elif n<=137:
#             return 32
#         elif n<=139:
#             return 33
#         elif n<=149:
#             return 34
#         elif n<=151:
#             return 35
#         elif n<=157:
#             return 36
#         elif n<=163:
#             return 37
#         elif n<=167:
#             return 38
#         elif n<=173:
#             return 39
#         elif n<=179:
#             return 40
#         elif n<=181:
#             return 41
#         elif n<=191:
#             return 42
#         elif n<=193:
#             return 43
#         elif n<=197:
#             return 44
#         elif n<=199:
#             return 45
#         elif n<=211:
#             return 46
#         elif n<=223:
#             return 47
#         elif n<=227:
#             return 48
#         elif n<=229:
#             return 49
#         elif n<=233:
#             return 50
#         elif n<=239:
#             return 51
#         elif n<=241:
#             return 52
#         elif n<=251:
#             return 53
#         elif n<=257:
#             return 54
#         elif n<=263:
#             return 55
#         elif n<=269:
#             return 56
#         elif n<=271:
#             return 57
#         elif n<=277:
#             return 58
#         elif n<=281:
#             return 59
#         elif n<=283:
#             return 60
#         elif n<=293:
#             return 61
#         elif n<=307:
#             return 62
#         elif n<=311:
#             return 63
#         elif n<=313:
#             return 64
#         elif n<=317:
#             return 65
#         elif n<=331:
#             return 66
#         elif n<=337:
#             return 67
#         elif n<=347:
#             return 68
#         elif n<=349:
#             return 69
#         elif n<=353:
#             return 70
#         elif n<=359:
#             return 71
#         elif n<=367:
#             return 72
#         elif n<=373:
#             return 73
#         elif n<=379:
#             return 74
#         elif n<=383:
#             return 75
#         elif n<=389:
#             return 76
#         elif n<=397:
#             return 77
#         elif n<=401:
#             return 78
#         elif n<=409:
#             return 79
#         elif n<=419:
#             return 80
#         elif n<=421:
#             return 81
#         elif n<=431:
#             return 82
#         elif n<=433:
#             return 83
#         elif n<=439:
#             return 84
#         elif n<=443:
#             return 85
#         elif n<=449:
#             return 86
#         elif n<=457:
#             return 87
#         elif n<=461:
#             return 88
#         elif n<=463:
#             return 89
#         elif n<=467:
#             return 90
#         elif n<=479:
#             return 91
#         elif n<=487:
#             return 92
#         elif n<=491:
#             return 93
#         elif n<=499:
#             return 94
#         elif n<=503:
#             return 95
#         elif n<=509:
#             return 96
#         elif n<=521:
#             return 97
#         elif n<=523:
#             return 98
#         elif n<=541:
#             return 99
#         elif n >541: 
#             ans = 100
#             key_list = [
#                 i for i in range(n) if 
#                 i!=1    and i%2!=0 and  i%3!=0 and  i%5!=0 and  i%7!=0 and  i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0 and i%23!=0 and i%29!=0 and i%31!=0 and i%37!=0 and 
#                 i%41!=0 and i%43!=0 and i%47!=0 and i%53!=0 and i%59!=0 and i%61!=0 and i%67!=0 and i%71!=0 and i%73!=0 and i%79!=0 and i%83!=0 and i%89!=0 and i%97!=0 and 
#                 i%101!=0 and i%103!=0 and i%107!=0 and i%109!=0 and i%113!=0 and i%127!=0 and i%131!=0 and i%137!=0 and i%139!=0 and i%149!=0 and i%151!=0 and i%157!=0 and 
#                 i%163!=0 and i%167!=0 and i%173!=0 and i%179!=0 and i%181!=0 and i%191!=0 and i%193!=0 and i%197!=0 and i%199!=0 and i%211!=0 and i%223!=0 and i%227!=0 and 
#                 i%229!=0 and i%233!=0 and i%239!=0 and i%241!=0 and i%251!=0 and i%257!=0 and i%263!=0 and i%269!=0 and i%271!=0 and i%277!=0 and i%281!=0 and i%283!=0 and 
#                 i%293!=0 and i%307!=0 and i%311!=0 and i%313!=0 and i%317!=0 and i%331!=0 and i%337!=0 and i%347!=0 and i%349!=0 and i%353!=0 and i%359!=0 and i%367!=0 and 
#                 i%373!=0 and i%379!=0 and i%383!=0 and i%389!=0 and i%397!=0 and i%401!=0 and i%409!=0 and i%419!=0 and i%421!=0 and i%431!=0 and i%433!=0 and i%439!=0 and 
#                 i%443!=0 and i%449!=0 and i%457!=0 and i%461!=0 and i%463!=0 and i%467!=0 and i%479!=0 and i%487!=0 and i%491!=0 and i%499!=0 and i%503!=0 and i%509!=0 and 
#                 i%521!=0 and i%523!=0 and i%541!=0
#             ]
#             key_value = int(n**(0.5))+1
#             for j in key_list:
#                 # print('j',j)
#                 for i in range(min(541, key_value-1), key_value):
#                     # print('i',i)
#                     if j%i==0 and j!=i:
#                         # print(i,j)
#                         break
#                 if i == key_value-1:
#                     ans += 1
#             return ans
        


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Step 1
        is_prime = [True] * n
        
        # Step 2
        is_prime[0] = is_prime[1] = False
        
        # Step 3
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # Step 4
        return sum(is_prime)



from time import time 
start = time()
ans = Solution()
ans.countPrimes(n=n)
end = time()
end-start



#######################
s = "  hello world  "       # Output: "world hello"
s = "a good   example"      # Output: "example good a"
s = "  Bob    Loves  Alice   "
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        # s = s.replace("  ", "")
        key_list = s.split(" ")
        key_list = [x for x in key_list if x != '']
        key_list.reverse()
        ans = ""
        for index, num in enumerate(key_list):
            if index!=len(key_list)-1: 
                ans = ans+num+" "
            else:
                ans = ans+num
        return ans
    




#######################
nums = [1,1,1,2,2,3]    ;   k = 2 # Output: [1,2]

import collections

class Solution:
    def topKFrequent(self, nums, k):
        key_list = collections.Counter(nums).most_common()
        return [i[0] for i in key_list[:k]]
    
#######################
nums = [4,3,2,7,8,2,3,1]    # Output: [2,3]

class Solution:
    def findDuplicates(self, nums):
        key_list = collections.Counter(nums).most_common()
        return [i[0] for i in key_list if i[1]>1]


#######################

nums = [1,2,3,4,5,6,7]  ;   k = 3   # Output: [5,6,7,1,2,3,4]

# The key thinking of this problem is ~
# 1) Using insert instead of append.
# 2) How to insert a list instead of a value?
# 3) Because 2 is not available, you MUST change to use the EXTEND method.
# Namely, we don't remove the tail, we'll remove the head
#                           and finally, we extend to the tail

class Solution:
    def rotate(self, nums, k):
        if k>=len(nums):
            k = k%len(nums)
        key_sublist = nums[:-k]
        del nums[:-k]
        nums.extend(key_sublist)


#######################
nums = [3,2,3]  # Output: [3]
nums = [1]      # Output: [1]
nums = [1,2]    # Output: [1,2]

import collections
from math import floor

class Solution:
    def majorityElement(self, nums):
        time_limit = int(floor(len(nums)/3))
        key_list = collections.Counter(nums).most_common()
        return [i[0] for i in key_list if i[1]>time_limit]
    

#######################
nums = [10,9,2,5,3,7,101,18]    # Output: 4
nums = [0,1,0,3,2,3]            # Output: 4
nums = [7,7,7,7,7,7,7]          # Output: 1

from numpy import array

class Solution:
    def lengthOfLIS(self, nums):
        nums = list(set(nums))
        nums.sort()
        key_list = nums[1:]
        key_list = array(key_list)
        origin_list = array(nums[:-1])
        key_list-origin_list


#######################

s = "abc"       ;   t = "ahbgdc"    # Output: true
s = "aaaaaa"    ;   t = "bbaaaa"
s = "ab"        ;   t = "baab"      # s in t
s = "ab"        ;   t = "baacb"     # s in t
s = "axc"       ;   t = "ahbgdc"    # 
s = "leeeeetcode"
t = "yyyyylyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyytyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyycyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyoyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyydyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
len(t)

'axc'.find('x',1)
t.count('e')
t.find('e',4)
t.find('t')
t.find('c')
t.find('o')
t.find('d')
t.find('e',1)

t.count('e')
'aaaaa'.find('a',2)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True                 # print(True)
        elif len(s) == len(t) and s!=t:
            return False         
        else:
            key_list = []
            try:
                key_list.append(t.find(s[0]))
            except:
                return False            # print(False)    
            
            
            for element in s[1:]:
                if element not in t:
                    return False        # print(False)
                for element2 in range(t.count(element)):
                    if t.find(element, element2)>key_list[-1]:
                        key_list.append(t.find(element, element2))
                        print(key_list)
                        t = t[:t.find(element, element2)]+'1'+t[t.find(element, element2)+1:]
                        break
                    elif element2 == t.count(element)-1:
                        return False    # print(False)
                    elif t.find(element, element2)<key_list[-1]:
                        t = t[:t.find(element, element2)]+'1'+t[t.find(element, element2)+1:]

            return True                 # print(True)
        
        
ans = Solution()
ans.isSubsequence(s=s, t=t)



######################################

nums = [1,2,3,1]    ;   indexDiff = 3   ;    valueDiff = 0  # Output: true

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        for index, num in enumerate(nums[:-indexDiff]):
            if nums[index+indexDiff] - num == valueDiff:
                return True
        return False




######################################

x = 123     # Output: 321
x = -123    # Output: -321
x = 120     # Output: 21

class Solution:
    def reverse(self, x):
        x = str(x)[::-1]
        try:
            return int(x) if -2**31<=int(x)<=2**31-1 else 0
        except:
            return -int(x[:-1]) if -2**31<=-int(x[:-1])<=2**31-1 else 0
        



######################################


strs = ["flower","flow","flight"]   # Output: "fl"
strs = ["dog","racecar","car"]      # Output: ""

class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort()
        key_list = [strs[n] for n in (0,-1)]
        k = 0
        for _ in range(len(key_list[0])):
            if key_list[0][k] == key_list[1][k]:
                k = k + 1
                continue
            else:
                break
        return key_list[0][:k]
    
ans = Solution()
ans.longestCommonPrefix(strs=strs)




######################################
x = 2.00000 ;   n = 10      # Output: 1024.00000
x = 2.10000 ;   n = 3       # Output: 9.26100
x = 2.00000 ;   n = -2      # Output: 0.25000

class Solution:
    def myPow(self,x: float, n: int) -> float:
        return x**n
    



#################################
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]


class Solution:
    def isNumber(self, s: str) -> bool:
        int("-90E3")