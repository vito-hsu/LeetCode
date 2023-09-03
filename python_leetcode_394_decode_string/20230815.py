
s = "3[a]2[bc]"         # "aaabcbc"
s = "3[a2[c]]"          # "accaccacc"
s = "2[abc]3[cd]ef"     # "abcabccdcdcdef"
s = "abc3[cd]xyz"       # "a"+"b"+"c"+3*("c"+"d")+"x"+"y"+"z"
s = "100[leetcode]"     # +100*("l"+"e"+"e"+"t"+"c"+"o"+"d"+"e")

import re

class Solution:
    def decodeString(self, s: str) -> str:  
        pattern = re.compile("^[a-z]+$")
        s = s.replace('[', '*(').replace(']', ')')
        key_string = ''

        for index, s_ele in enumerate(s):
            if s_ele.isdigit() and s[index-1].isdigit():
                key_string = key_string + f'{s_ele}'
            elif s_ele.isdigit():
                key_string = key_string + f'+{s_ele}'
            elif pattern.match(s_ele) and (s[index-1]=='(' or index == 0):
                key_string = key_string + f'"{s_ele}"'
            elif pattern.match(s_ele):
                key_string = key_string + f'+"{s_ele}"'
            else:
                key_string = key_string + f'{s_ele}'

        return eval(key_string)