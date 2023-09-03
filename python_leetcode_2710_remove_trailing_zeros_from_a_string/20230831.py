num = "51230100"        # Output: "512301"


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while num[len(num)-1]=='0':
            num = num[:len(num)-1]
        return num