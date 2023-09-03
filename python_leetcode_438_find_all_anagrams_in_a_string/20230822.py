s = "cbaebabacd" ; p = "abc"    # Output: [0,6]
s = "abab" ; p = "ab"           # Output: [0,1,2]
s = "a" ; p = "ab"

class Solution:
    def findAnagrams(self, s: str, p: str):
        p_len = len(p)
        s_len = len(s)
        compare1 = list(p)
        compare1.sort()
        ans_list = []
        for num in range(s_len-p_len+1):    # num = 0
            compare2 = list(s[num:num+p_len])
            compare2.sort()
            if compare1==compare2:
                ans_list.append(num)
        return ans_list