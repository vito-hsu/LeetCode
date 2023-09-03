sentence = "thequickbrownfoxjumpsoverthelazydog"        # Output: true

import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        our_list = list(string.ascii_lowercase)
        if all([char in sentence for char in our_list]):
            return True
        else:
            return False