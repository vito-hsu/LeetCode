haystack = "sadbutsad"; needle = "sad"  # Output: 0
haystack = "leetcode"; needle = "leeto" # Output: -1


class Solution:
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        elif needle in haystack:
            return haystack.find(needle)
            # haystack.replace(needle, "0"*len(needle)).index(0)