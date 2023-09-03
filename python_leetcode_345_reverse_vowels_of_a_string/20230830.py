s = "hello"         # Output: "holle"

import numpy as np

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = np.array(list(s))
        v_list_ind = np.where((s=="a" )|(s=="e")|(s=="i")|(s=="o")|(s=="u")|(s=="A")|(s=="E")|(s=="I")|(s=="O")|(s=="U"))
        v_list = s[v_list_ind]
        v_list_rev = v_list[::-1]
        s[v_list_ind] = v_list_rev
        return ''.join(list(s))