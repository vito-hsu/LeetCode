arr = [-3,0,1,-3,1,1,1,-3,10,0]     # Output: true


import collections

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        all_count = [count for num, count in collections.Counter(arr).most_common()]
        if len(set(all_count))==len(all_count):
            return True
        else:
            return False

