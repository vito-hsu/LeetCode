ransomNote = "a" ; magazine = "b"           # Output: false
ransomNote = "aa" ; magazine = "ab"         # Output: false
ransomNote = "aa" ; magazine = "aab"         # Output: true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        while len(ransomNote)>0:
            key_num = ransomNote[0]
            if ransomNote.count(key_num) <= magazine.count(key_num):
                ransomNote = ransomNote.replace(key_num, "")
                magazine = magazine.replace(key_num, "")
            else:
                return False
        return True