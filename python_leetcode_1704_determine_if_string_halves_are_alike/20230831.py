s = "book"          # Output: true
s = "textbook"      # Output: false
s = "AbCdEfGh"      # 


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s1 = s[:int(len(s)/2)]
        s2 = s[int(len(s)/2):]
        s1_set = set(s1)
        s2_set = set(s2)
        ans1 = 0
        ans2 = 0

        for vowel in vowels:
            if vowel in s1_set:
                ans1+=s1.count(vowel)
            if vowel in s2_set:
                ans2+=s2.count(vowel)
        return True if ans1==ans2 else False
            