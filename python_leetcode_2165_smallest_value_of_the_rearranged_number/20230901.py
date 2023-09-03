num = 310           # Output: 103
num = -7605         # Output: -7650

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0       

        if num>0:
            key_list = list(str(num))
            key_list.sort()
            # key_index = [ind for ind, ele in enumerate(key_list) if ele!="0"][0]
            key_index = next((ind for ind, ele in enumerate(key_list) if ele!="0"), None)
            key_num = next((ele for ind, ele in enumerate(key_list) if ele!="0"), None)  
            key_list.pop(key_index)
            key_list.insert(0, key_num)
            return int("".join(key_list))
        else:
            key_list = list(str(num)[1:])
            key_list.sort(reverse=True)
            return int("-"+"".join(key_list))