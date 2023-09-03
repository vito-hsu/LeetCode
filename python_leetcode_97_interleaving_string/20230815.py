s1 = "aabcc" ; s2 = "adbbca" ; s3 = "aadabbcbcac"
s1 = "aabcc" ; s2 = "adbbca" ; s3 = "aabadbcbcac"   # s3_element = s3[0]
s1 = "aabcc" ; s2 = "aabbca" ; s3 = "aabbaabccca"
s1 = "aabcc" ; s2 = "aabbca" ; s3 = "aabaabbccca"
s1 = "aabcc" ; s2 = "aabbca" ; s3 = "aabababccca"
s1 = "aabac" ; s2 = "aabbca" ; s3 = "aabababacca"

s1 = "aabcc" ; s2 = "dbbca" ; s3 = "aadbbbaccc"  # false

s1 = "" ; s2 = "" ; s3 = ""   # true

s1 = "accbaabaaabbcbaacbababacaababbcbabaababcaabbbbbcacbaa"
s2 = "cabaabcbabcbaaaacababccbbccaaabaacbbaaabccacabaaccbbcbcb"
s3 = "accbcaaabbaabaaabbcbcbabacbacbababaacaaaaacbabaabbcbccbbabbccaaaaabaabcabbcaabaaabbcbcbbbcacabaaacccbbcbbaacb"


import random

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        o1 = s1 ; o2 = s2 ; o3 = s3
        for k in range(1000):
            # print(k)
            s1 = o1 ; s2 = o2 ; s3 = o3
            for s3_element in s3:
                if len(s1)>0 and len(s2)>0 and s3_element == s1[0] and s3_element == s2[0]:
                    key_1 = next((char for char in s1 if char != s1[0]), None)
                    key_2 = next((char for char in s2 if char != s2[0]), None)
                    key_3 = next((char for char in s3 if char != s3[0]), None)
                    if key_1 == key_2 == key_3:
                        if random.random()>0.5:
                            s1 = s1[1:] ; s3 = s3[1:]
                        else:
                            s2 = s2[1:] ; s3 = s3[1:]
                    elif key_1 == key_3:
                        s1 = s1[1:] ; s3 = s3[1:]
                    elif key_2 == key_3:
                        s2 = s2[1:] ; s3 = s3[1:]
                elif len(s1)>0 and s3_element == s1[0]:
                    s1 = s1[1:] ; s3 = s3[1:]
                elif len(s2)>0 and s3_element == s2[0]:
                    s2 = s2[1:] ; s3 = s3[1:]
                else:
                    continue
            if s1=="" and s2=="" and s3=="":
                return True # print("return true")
        
        return False


ans = Solution()
ans.isInterleave(s1=s1, s2=s2, s3=s3)