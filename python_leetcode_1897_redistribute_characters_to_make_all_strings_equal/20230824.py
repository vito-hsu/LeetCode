words = ["abc","aabc","bc"]     # Output: true


class Solution:
    def makeEqual(self, words) -> bool:
        key_word = ''.join(words)
        key_set  = set(key_word)
        for num in key_set:             # num = next(iter(key_set))
            if key_word.count(num)%len(words)!=0:
                return False
        return True