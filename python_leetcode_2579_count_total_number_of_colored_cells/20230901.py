# 1+0+0+0
# 2+1+1+1
# 3+2+2+2

n = 2       # Output: 5

def colored_cells(n):
    if n==1:
        return 1
    else:
        key_ans = 4*(n-1)
        return colored_cells(n-1)+key_ans

class Solution:
    def coloredCells(self, n: int) -> int:
        return colored_cells(n=n)