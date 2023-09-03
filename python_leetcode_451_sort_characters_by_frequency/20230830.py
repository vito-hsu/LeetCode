s = "tree"          # Output: "eert"

import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        key_list = collections.Counter(s).most_common()
        return "".join([char*count for char, count in key_list])