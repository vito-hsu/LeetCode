from itertools import combinations_with_replacement

def generate_combinations(arr, n):
    return list(combinations_with_replacement(arr, n))

# # 测试
# arr = ['a','e','i','o','u']
# n = 2
# combinations = generate_combinations(arr, n)
# result = [''.join(comb) for comb in combinations]
# len(result)


class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = ['a','e','i','o','u']
        combinations = generate_combinations(arr, n)
        result = [''.join(comb) for comb in combinations]
        return len(result)