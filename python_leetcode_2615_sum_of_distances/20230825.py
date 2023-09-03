nums = [1,3,1,1,2]      # Output: [5,0,3,4,0]

with open(r"C:\Users\vito\Desktop\leetcode_0825.txt", 'r') as file:
    content = file.read()
nums = eval(content)

import numpy as np
from scipy.spatial.distance import pdist, squareform



class Solution:
    def distance(self, nums):
        ans_list    = np.array([0]*len(nums))
        key_set     = set(nums)
        nums        = np.array(nums)

        for ind, num in enumerate(nums):            # ind=0;num=nums[0]
            if (num not in key_set) or (ans_list[ind]!=0):
                continue
            else:
                key_indices     = np.where(nums==num)[0]    # len(key_indices)
                points          = key_indices.reshape(-1, 1)
                distances       = pdist(points, metric='cityblock')  # 使用曼哈顿距离
                dist_matrix     = squareform(distances)
                sum_distances   = np.sum(dist_matrix, axis=1)            
                ans_list[key_indices] = sum_distances
        
        return ans_list
    












import numpy as np
from scipy.spatial.distance import pdist

points = np.array([0, 2, 3]).reshape(-1, 1)
distances = pdist(points, metric='cityblock')

sum_distances = []
for i in range(len(points)):
    mask = np.ones(len(points), dtype=bool)
    mask[i] = False
    sum_distances.append(np.sum(distances[mask]))

sum_distances = np.array(sum_distances)
print(sum_distances)
