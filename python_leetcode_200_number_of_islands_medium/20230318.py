grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]   # Output: 1

grid = [["1"],["1"]]        # Output: 1

grid = [["1","1","1"],["0","1","0"],["1","1","1"]]  # Output: 1

grid = [["1","0","1","1","0","1","1"]]

import numpy as np

def key_deletion(grid, index):              # index = [0,0]
    grid[index[0],index[1]]='0'
    try:        # check right
        if grid[index[0],index[1]+1]=='1':
            new_index = [index[0],index[1]+1]
            key_deletion(grid, new_index)  
    except:
        pass
    try:        # check down
        if grid[index[0]+1, index[1]]=='1':
            new_index_2 = [index[0]+1, index[1]]
            key_deletion(grid, new_index_2)
    except:
        pass
    try:        # up
        if grid[index[0]-1, index[1]]=='1' and index[0]!=0:
            new_index_3 = [index[0]-1, index[1]]
            key_deletion(grid, new_index_3)
    except:
        pass
    try:        # left
        if grid[index[0], index[1]-1]=='1' and index[1]!=0:
            new_index_4 = [index[0], index[1]-1]
            key_deletion(grid, new_index_4)
    except:
        pass


class Solution:
    def numIslands(self, grid):
        grid = np.array(grid)
        ans = 0
        key_list = np.array(np.where(grid=="1")).T.tolist()                 # transpose is very very important~~!!!
        for num in key_list:        # num = key_list[0]
            if grid[num[0], num[1]]!='0':
                key_deletion(grid=grid, index=num)
                ans += 1
        return ans

ans = Solution()
ans.numIslands(grid=grid)