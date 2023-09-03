a = 1 ; b = 2        # Output: "abb"
a = 4 ; b = 1        # Output: "abb"
a = 55 ; b = 45        # Output: "abb"
a = 1 ; b = 1        # Output: "ab"


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ''
        while a+b>0:
            # print(ans, a, b)
            if len(ans)==0:
                if a>b>0:
                    ans += "aa"
                    a = a - 2
                elif b>a>0:
                    ans += "bb"
                    b = b -2
                elif a>b==0:
                    ans += a*"a"
                    a = a - a
                elif b>a==0:
                    ans += b*"b"
                    b = b - b
                elif a==b>0:
                    ans += "a"
                    a = a - 1
                print('cont.')
                continue
            if a>b and ans[-1]=="b":
                if a>1:
                    ans += "a"*2 
                    a = a - 2
                else:
                    ans += "a"
                    a = a - 1
                    return ans
            elif b>a and ans[-1]=="a":
                if b>1:
                    ans += "b"*2
                    b = b - 2
                else:
                    ans += "b"
                    b = b - 1
                    return ans
            elif ans[-1]=="b":
                ans += "a"
                a = a - 1
            elif ans[-1]=="a":
                ans += "b"
                b = b -1
            else:
                print("################################################")
        return ans
            
ans1 = Solution()
ans1.strWithout3a3b(a=a, b=b)