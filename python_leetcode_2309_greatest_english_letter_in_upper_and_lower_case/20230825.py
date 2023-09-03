
s = "lEeTcOdE"          # Output: "E"

import string

class Solution:
    def greatestLetter(self, s: str) -> str:
        key_dict = {a:b for a,b in zip(string.ascii_lowercase,string.ascii_uppercase)}
        s_set    = set(s)
        ans_list = []
        for s_ele in s_set:
            try:
                if key_dict[s_ele] in s_set:
                    ans_list.append(s_ele)
            except:
                pass

        return key_dict[max(ans_list)] if len(ans_list)>0 else ""