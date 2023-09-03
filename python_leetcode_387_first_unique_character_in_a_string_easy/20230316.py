s = "leetcode"      # Output: 0
s = "loveleetcode"  # Output: 2
s = "aabb"          # Output: -1


import collections

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for index, num in enumerate(list(s)):
#             if list(s).count(num) == 1:
#                 return index
#             else:
#                 continue
#         return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        key_list = [i[0] for i in collections.Counter(s).most_common() if i[1]==1]
        ans_list = []
        for i in key_list:
            ans_list.append(list(s).index(i))
        return min(ans_list) if ans_list != [] else -1

ans = Solution()
ans.firstUniqChar(s=s)