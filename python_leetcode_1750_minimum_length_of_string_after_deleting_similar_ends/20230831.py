s = "cabaabac"      # Output: 0
s = "aabccabba"     # Output: 3
s = "ca"            # Output: 2
s = "aa"            # Output: 0


def first_not_num(s,num):
    for ind,ele in enumerate(s):
        if ele!=num:
            return ind


class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s)!=0:
            if len(s)==1:
                return 1

            if s == s[0]*len(s) and len(s)!=1:
                return 0
            
            s0 = s[0]
            key_value1 = first_not_num(s, s0)
            key_value2 = first_not_num(s[::-1], s0)
            
            if key_value1*key_value2!=0:
                s = s[key_value1:-(key_value2)]
            else:
                break
        return len(s)