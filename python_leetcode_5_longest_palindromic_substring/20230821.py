s = "babad"     # "bab"
s = "cbbd"      # "bb"
s = "abb"       # "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for num in range(len(s),0,-1):                  # num = 2
            key_subs = s[:num]
            key_num  = len(s)-num+1
            for i in range(1,key_num+1):
                if key_subs == key_subs[::-1]:
                    print(key_subs)#return key_subs
                else:
                    key_subs = s[i:num+i]
                