s = "bcabc"             # "abc"
s = "cbacdcbc"          # "acdb"

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        










































































        
# bisect.bisect_left(['b', 'c', 'a', 'c', 'b'], 'b')       # 3
# bisect.bisect_left(['b', 'c', 'a', 'c', 'b'], 'c')       # 5
# bisect.bisect_left(['b', 'c', 'a', 'c', 'b'], 'a')       # 0

# bisect.bisect_left(["c","b","a","c","d","c","b","c"], 'a')       # 0
# bisect.bisect_left(["c","b","a","c","d","c","b","c"], 'b')       # 3
# bisect.bisect_left(["c","b","a","c","d","c","b","c"], 'c')       # 3
# bisect.bisect_left(["c","b","a","c","d","c","b","c"], 'd')       # 4

# bisect.bisect_left(["c","b","a","b","d","c","b","c"], 'a')       # 0
# bisect.bisect_left(["c","b","a","b","d","c","b","c"], 'b')       # 3
# bisect.bisect_left(["c","b","a","b","d","c","b","c"], 'c')       # 4
# bisect.bisect_left(["c","b","a","b","d","c","b","c"], 'd')       # 4

# bisect.bisect_left(["e","b","a","b","d","c","b","e"], 'a')       # 0
# bisect.bisect_left(["e","b","a","b","d","c","b","e"], 'b')       # 3
# bisect.bisect_left(["e","b","a","b","d","c","b","e"], 'c')       # 4
# bisect.bisect_left(["e","b","a","b","d","c","b","e"], 'd')       # 4
# bisect.bisect_left(["e","b","a","b","d","c","b","e"], 'e')       # 7

# bisect.bisect(["e","b","a","e","b","d","c","b"], 'a')       # 3
# bisect.bisect(["e","b","a","e","b","d","c","b"], 'b')       # 5
# bisect.bisect(["e","b","a","e","b","d","c","b"], 'c')       # 8
# bisect.bisect(["e","b","a","e","b","d","c","b"], 'd')       # 8
# bisect.bisect(["e","b","a","e","b","d","c","b"], 'e')       # 8


# import bisect

# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         sort_list = sorted(list(set(s)))
#         key_list = []
#         for num in sort_list:
#             key_list.append(bisect.bisect_left(list(s), num))
        
#         ans_list = []
#         for index, element in enumerate(key_list):
#             if element != key_list[index+1] and element != key_list[index-1]:
#                 ans_list.append(element)
#             elif element == key_list[index+1]:
#                 ans_list.append(key_list[index+1])
#             elif element == key_list[index-1]:
#                 ans_list.append(key_list[index-1])
#             else:

