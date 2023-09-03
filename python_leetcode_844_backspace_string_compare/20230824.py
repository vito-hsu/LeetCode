s = "ab#c" ; t = "ad#c"  # Output: true
s = "ab##" ; t = "c#d#"  # Output: true

s = "xywrrmp"
t = "xywrrmu#p"  # Output: true

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while '#' in s:
            del_ind = s.index('#')
            key_del = max(del_ind-1,0)
            s = s[:key_del]+s[del_ind+1:]

        while '#' in t:
            del_ind = t.index('#')
            key_del = max(del_ind-1,0)
            t = t[:key_del]+t[del_ind+1:] 

        if s == t:
            return True
        else:
            return False