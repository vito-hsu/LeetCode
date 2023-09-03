s = "   -42"                # Output: -42
s = "4193 with words"       # Output: 4193
s = "wor2s and 987"
s = "41.93 with words"
s = "-91283472332"
s = "-9128347233233333333333333333333333"
s = ".1"
s = "+-12"
s = "  0000000000012345678"
s = "    0000000000000   "
s = "-000000000000001"


class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="":
            return 0

        try:
            while s[0]==" " or s[0]=="0":
                s = s[1:]
        except:
            return 0

        s = s.split(" ")[0]

        try:
            eval(s)
        except:
            try:
                int(s)
            except:
                return 0

        if "." in s:
            key_index = s.index(".")
            s = s[:key_index]

        if s=="":
            return 0
        
        if "+" in s and "-" in s:
            return 0
        
        if eval(s)<0:
            if eval(s)<-2**31:
                return -2**31
            else:
                return eval(s)
        else:         
            if eval(s)>2**31-1:
                return 2**31-1           # int(41.8) ; int(41.84) ; eval("41.2")
            else:
                return eval(s)

            