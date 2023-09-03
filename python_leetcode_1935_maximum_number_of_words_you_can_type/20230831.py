text = "hello world" ; brokenLetters = "ad"      # Output: 1


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # key_set = set(brokenLetters)
        ans = 0
        key_list = text.split(" ")
        for ele in key_list:        # ele = key_list[0]
            if not any(char in ele for char in brokenLetters):
                ans += 1
        return ans