barcodes = [1,1,1,2,2,2]        # Output: [2,1,2,1,2,1]
barcodes = [1,1,1,1,2,2,3,3]    # Output: [1,3,1,3,1,2,1,2]

f = open('data.txt', 'r')
data = f.read()
data = data.split('\n')             # len(data)
barcodes = eval(data[0])            # len(barcodes)
f.close()


from collections import Counter
from time import time

def key_function(barcodes):
    ans_list = [-1]
    key_value = 1
    key_list = [list(num) for num in Counter(barcodes).most_common()]   # len(key_list)

    while barcodes!=[]:
        ans = -1
        for index, num in enumerate(key_list):      
            if num[0]!=ans_list[-1] and num[1]>0:
                ans = num[0]
                key_list[index][1] -= 1
                break
            
        if ans!= -1:
            ans_list.append(ans)
            barcodes.remove(ans)

        if ans == -1:
            ans = Counter(barcodes).most_common()[0][0]
            ans_list.insert(key_value,ans)                  # key_value is here~~
            key_value+=2
            barcodes.remove(ans)

    return ans_list[1:]


class Solution:
    def rearrangeBarcodes(self, barcodes):
        return key_function(barcodes=barcodes)

ans = Solution()
start = time()
ans.rearrangeBarcodes(barcodes=barcodes)
end = time()
end - start