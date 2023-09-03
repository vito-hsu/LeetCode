words = ["cd","ac","dc","ca","zz"]          # Output: 2
words = ["ab","ba","cc"]                    # Output: 1



class Solution:
    def maximumNumberOfStringPairs(self, words) -> int:
        key_list = [list(word) for word in words]
        key_list = [tuple(sorted(word)) for word in words]
        key_num  = len(set(key_list))
        return len(words)-key_num