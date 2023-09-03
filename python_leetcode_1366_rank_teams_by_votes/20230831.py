votes = ["ABC","ACB","ABC","ACB","ACB"]     # Output: "ACB"
votes = ["WXYZ","XYZW"]                     # Output: "XWYZ"
votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]      # Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]



import numpy as np

class Solution:
    def rankTeams(self, votes) -> str:
        key_list1 = list(votes[0])
        key_list1.sort()
        key_list2 = [num for num in range(len(votes[0]))]
        key_set = dict(zip(key_list1, key_list2))
        ans = np.array(([0]*len(votes[0]))*len(votes[0]))
        ans = ans.reshape(len(votes[0]),len(votes[0]))  # reshape
        ans = ans.tolist()
        for vote in votes:
            for ind, s in enumerate(vote):
                ans[key_set[s]][ind] += 1
        ans_set = dict(zip(key_list1,ans))
        ans.sort(reverse=True)
        ans_string = ""
        for ele in ans:
            for key, value in ans_set.items():
                if value == ele:
                    ans_string+=key
                    del ans_set[key]
                    break
        return ans_string





