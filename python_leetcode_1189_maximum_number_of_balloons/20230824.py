text = "nlaebolko"              # Output: 1
text = "loonbalxballpoon"       # Output: 2
text = "leetcode"               # Output: 0


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_num = text.count('b')
        a_num = text.count('a')
        l_num = int(text.count('l')/2)
        o_num = int(text.count('o')/2)
        n_num = text.count('n')
        return min(b_num, a_num, l_num, o_num, n_num)