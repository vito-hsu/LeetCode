num = 9669      # Output: 9969



class Solution:
    def maximum69Number (self, num: int) -> int:
        key_string = list(str(num))
        for ind, s in enumerate(key_string):
            if s == "6":
                key_string[ind] = "9"
                return int("".join(key_string))
            
        return num