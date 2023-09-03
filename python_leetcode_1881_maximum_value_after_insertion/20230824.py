n = "99" ; x = 9        # Output: "999"
n = "12" ; x = 9        # Output: "912"
n = "-13" ; x = 2       # Output: "-123"
n = "-11" ; x = 2       # Output: "-112"
n = "9898" ; x = 9      # Output: "99898"
n = "-1315" ; x = 3     # Output: "-13135"

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0]=='-':
            new_n = n[1:]
            for ind, num in enumerate(new_n):
                if x<int(num):
                    print('-'+new_n[:ind]+str(x)+new_n[ind:])# return '-'+new_n[:ind]+str(x)+new_n[ind:]
            print(n+str(x))
        else:
            for ind, num in enumerate(n):
                if x>int(num):
                    print(n[:ind]+str(x)+n[ind:])# return n[:ind]+str(x)+n[ind:]
            print(n+str(x))


































# class Solution:
#     def maxValue(self, n: str, x: int) -> str:
#         if int(n)>0:
#             ans = 0
#             for ind in range(len(n)):       # ind = 0
#                 new = n[:ind]+str(x)+n[ind:]
#                 if int(new)>ans:
#                     ans = int(new)


#         else:
#             ans = int("-"+"9"*(10**6))           # int(ans)
#             for ind in range(len(n)):       # ind = 0
#                 new = n[:ind+1]+str(x)+n[ind+1:]
#                 if int(new)>ans:
#                     ans = int(new)
    
#         return str(ans)