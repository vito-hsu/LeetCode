str1 = "ABCABC" ; str2 = "ABC"       # Output: "ABC"
str1 = "ABABAB" ; str2 = "ABAB"      # Output: "AB"
str1 = "LEET" ; str2 = "CODE"        # Output: ""


import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)

        

        key_num  = math.gcd(str1_len, str2_len)
        common_factors = [i for i in range(1, key_num+1) if str1_len % i == 0 and str2_len % i == 0]
        common_factors.sort(reverse=True)

        for i in common_factors:        # i=3
            if str1[:i]*int(str1_len/i)==str1 and str2[:i]*int(str2_len/i)==str2 and str1[:1]==str2[:1]:
                return str1[:i]
        return ""