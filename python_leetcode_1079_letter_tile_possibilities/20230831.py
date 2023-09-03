tiles = "AAB"       # Output: 8

import itertools

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        key_list = [p for length in range(1, len(tiles)+1) for p in itertools.permutations(tiles, length)]
        return len(set(key_list))





# from itertools import permutations
# string = 'AAC'
# permutations_list = [p for length in range(1, 4) for p in permutations(string, length)]
# print(permutations_list)