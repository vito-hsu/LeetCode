words = ["bella","label","roller"]  # Output: ["e","l","l"]
words = ["cool","lock","cook"]      # Output: ["c","o"]

class Solution:
    def commonChars(self, words):
        key_word = words[0]
        words = words[1:]
        
        ans = []

        for char in key_word:                   # char = 'o'
            i = 0
            for ind, word in enumerate(words):
                if char in word:
                    words[ind] = word.replace(char, "", 1)
                    i += 1
                else:
                    break
            if i==len(words):
                ans.append(char)
    
        return ans