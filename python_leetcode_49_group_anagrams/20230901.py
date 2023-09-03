
strs = ["eat","tea","tan","ate","nat","bat"]            # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = [""]                                             # Output: [[""]]
strs = ["a"]                                            # Output: [["a"]]



class Solution:
    def groupAnagrams(self, strs):
        key_dict = {}
        start = 0
        ans_list = []
        for str in strs:            
            key_str = list(str)
            key_str.sort()
            key_str = "".join(key_str)
            if key_str not in key_dict:
                key_dict[key_str] = start
                start += 1
                ans_list.append([str])
            elif key_str in key_dict:
                ans_list[key_dict[key_str]].append(str)
        return ans_list