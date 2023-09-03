s = "abab"          # Output: true
s = "aba"           # Output: false
s = "abcabcabcabc"  # Output: true
s = "aaa"           # Output: true
a = "a"             # Output: true


def get_possible_key_numbers(s):
    num = len(s)
    factors = []

    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)

    return [factor for factor in factors if factor<=num/2]


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        key_numbers = get_possible_key_numbers(s)
        s_len       = len(s)
        for key_number in key_numbers:          # key_number = 1
            if s[:key_number]*int(s_len/key_number) == s:
                return True
        return False










