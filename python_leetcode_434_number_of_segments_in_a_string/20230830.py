s = "Hello, my name is John"        # Output: 5
s = ""                              # Output: 0
s = "                "

class Solution:
    def countSegments(self, s: str) -> int:
        key_list = s.split(" ")
        while "" in key_list:
            key_list.remove("")
        return len(key_list) 