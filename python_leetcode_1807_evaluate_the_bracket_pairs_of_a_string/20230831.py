s = "(name)is(age)yearsold" ; knowledge = [["name","bob"],["age","two"]]    # Output: "bobistwoyearsold"
s = "(a)(a)(a)aaa" ; knowledge = [["a","yes"]]                              # Output: "yesyesyesaaa"
s = "hi(name)" ; knowledge = [["a","b"]]                                    # Output: "hi?"
s = "(a)(a)(a)aaa(name)is(age)yearsold" ; knowledge = [["a","b"]]


import re 

class Solution:
    def evaluate(self, s: str, knowledge) -> str:
        if len(knowledge)==0:
            matches = set(re.findall(r'\(.*?\)', s))
            for m in matches:
                s = s.replace(m, '?')       
        else:     
            knowledge = dict(knowledge)
            matches = set(re.findall(r'\(.*?\)', s))
            for m in matches:                           # m = matches[0]
                if m[1:-1] in knowledge:  # 
                    s = s.replace(m, knowledge[m[1:-1]])
                else:
                    s = s.replace(m, '?')
        return s




