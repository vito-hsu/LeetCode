arr = [1,0,2,3,0,4,5,0]     # [1,0,0,2,3,0,0,4]


class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i<=len(arr)-1:
            if arr[i]!=0:
                i += 1
                continue
            else:
                arr.insert(i, 0)
                arr.pop()
                i += 2