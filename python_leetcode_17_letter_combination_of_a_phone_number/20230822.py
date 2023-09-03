digits = "23"   # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
digits = ""     # Output: []
digits = "2"    # Output: ["a","b","c"]


from itertools import product

class Solution:
    def letterCombinations(self, digits: str):
        if digits == "":
            return []

        strings = []

        hash_table = {
            '2':'abc',  '3':'def',  '4':'ghi', '5':'jkl',
            '6':'mno',  '7':'pqrs', '8':'tuv', '9':'wxyz'
        }
        
        for digit in digits:
            strings.append(hash_table[digit])

        return [''.join(combination) for combination in product(*strings)]



from itertools import product
strings = ["abc", "def", "ghi", "jkl"]  # 可以根据需要添加更多字符串
combinations_list = [''.join(combination) for combination in product(*["abc", "def", "ghi", "jkl"])]
print(combinations_list)