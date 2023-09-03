s1 = "ab" ; s2 = "eidbaooo" # Output: true
s1 = "ab" ; s2 = "eidboaoo" # Output: false


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        compare1 = list(s1)
        compare1.sort()
        ans = False 
        
        if len_s1>len_s2:
            print(False)#return False
        else:
            for num in range(len_s2-len_s1+1):    # num = 0
                compare2 = list(s2[num:num+len_s1])
                compare2.sort()
                if compare1==compare2:
                    print(True)#return True
        print(ans)#return ans