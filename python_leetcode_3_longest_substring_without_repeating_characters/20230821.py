s = "abcabcbb"      # Output: 3
s = "bbbbb"         # Output: 1
s = "pwwkew"        # Output: 3

len(s) ; len(set(s)) ; s[-1] ; s[3:]

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        key_string = ''
        ans = 0
        for s_ele in s:
            print(s_ele)
            key_string += s_ele
            if len(key_string) == len(set(key_string)):
                if len(key_string)>ans:
                    ans = len(key_string)
            else:
                key_index = key_string.index(key_string[-1])
                key_string = key_string[key_index+1:]
        return ans




# def find_first_duplicate_position_and_final_answer(s2):
#     for i, char in enumerate(s2):
#     #   print(i, char, s2[:i])
#       if i>0:
#         if char in s2[:i]:
#               return i
#     return len(s2)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         key_list = []
#         start = 0
#         end = len(set(s))
#         if len(set(s))<=1:
#             return len(set(s))
#         elif len(s)==len(set(s)):
#             return len(s)
#         else:
#             for _ in range(len(s)-len(set(s))+1):
#                 print(s[start:end])
#                 key_num = find_first_duplicate_position_and_final_answer(s[start:end])
#                 key_list.append(key_num)
#                 start+=1
#                 end+=1
#         print(key_list)
#         return max(key_list)