num = 430043    ; k = 2         # Output: 2
num = 240       ; k = 2         # Output: 2
num = 2         ; k = 1
num = 10        ; k = 1

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        ans = 0
        if k==1:
            for v in num_str:
                check_value = int(v)
                if check_value!=0:
                    if num%check_value==0:
                        ans+=1            
        else:
            for ind, v in enumerate(num_str[:-(k-1)]):
                check_value = int(num_str[ind:ind+k])
                if check_value!=0:
                    if num%check_value==0:
                        ans+=1
        return ans