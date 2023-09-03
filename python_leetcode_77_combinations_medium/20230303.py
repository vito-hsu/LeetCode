n = 4   ;   k = 2   # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
n = 1   ;   k = 1   # Output: [[1]]
n = 2   ;   k = 1   # Output: [[1],[2]]
n = 10  ;   k = 7

# If you want to do the nested n times problem, like combination, 
# I suggest you use the itertools as follows
import itertools
class Solution:
    def combine(self, n: int, k: int):
        ans = [[int(j) for j in list(item)] for item in itertools.combinations(range(1,n+1), k)]
        return ans

ans = Solution()
ans.combine(n=n, k=k)