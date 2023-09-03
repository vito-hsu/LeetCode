s = "paper" ;   t = "title"     # true
s = "egg"   ;   t = "add"       # true
s = "foo"   ;   t = "bar"       # false

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False

        key_list1 = []
        key_list2 = []
        
        for index, s_element in enumerate(s):
            if s_element not in key_list1:
                key_list1.append(s_element)
                key_list2.append(t[index])
            elif s_element in key_list1:
                key_index = [index for index, char in enumerate(key_list1) if char == s_element][0]
                if key_list2[key_index] != t[index]:
                    # print(False)
                    return False
                
        return True
    
ans = Solution()
ans.isIsomorphic(s=s, t=t)