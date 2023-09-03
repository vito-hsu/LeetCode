names = ["Mary","John","Emma"] ; heights = [180,165,170]     # Output: ["Mary","Emma","John"]

names = ["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
heights = [17233,32521,14087,42738,46669,65662,43204,8224]

names = ["GXLVEHVABFOGSFXUYYR","TUHxnsxmu","X","OOYBLVKmzlaeaxbprc","ARNLAPtfvmutkfsa","XPMKPDUWOQEEILtbdjip","QICEutjbr","R"]
heights = [11578,89340,73785,12096,55734,89484,59775,72652]


import numpy as np
import scipy.stats

class Solution:
    def sortPeople(self, names, heights):
        rank    = len(names)-1-(scipy.stats.rankdata(heights, method='min')-1)
        order   = np.argsort(rank)
        return np.array(names)[order].tolist()
    












# import numpy as np

# arr = np.array([7, 1, 2, 6, 5, 0, 4, 3])
# sorted_indices = np.argsort(arr)  # 取得由小到大的索引排序

# sorted_order = arr[sorted_indices]  # 使用排序後的索引取得排序後的陣列

# print(sorted_order)