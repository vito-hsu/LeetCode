words = ["one.two.three","four.five","six"] ; separator = "."        # Output: ["one","two","three","four","five","six"]
words = ["$easy$","$problem$"] ; separator = "$"                     # Output: ["easy","problem"]



class Solution:
    def splitWordsBySeparator(self, words, separator: str):
        ans_list = []
        for word in words:                      # word = "one.two.three"
            if separator in word:
                ans_list.extend(word.split(separator))
            else:
                ans_list.append(word)
        ans_list = [word for word in ans_list if word != ""]
        return ans_list