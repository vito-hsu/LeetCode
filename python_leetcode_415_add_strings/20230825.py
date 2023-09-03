num1 = "11" ; num2 = "123"              # Output: "134"
num1 = "456" ; num2 = "77"              # Output: "533"
num1 = "999" ; num2 = "1"               # Output: "1000"


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            num1, num2 = num2, num1

        rev_num1 = num1[::-1]
        rev_num2 = num2[::-1]
        ans_list = []
        
        plus = 0
        for ind, ele1 in enumerate(rev_num1):       # ind=1 ; ele='9'
            try:
                ele2 = rev_num2[ind]
            except:
                ele2 = 0
            ans = int(ele1)+int(ele2)+plus
            if ans>9:
                ans_list.append(str(ans)[1])
                plus=1
            else: 
                ans_list.append(str(ans))
                plus=0
            

        return ''.join(ans_list)[::-1] if ans<10 else '1'+''.join(ans_list)[::-1]