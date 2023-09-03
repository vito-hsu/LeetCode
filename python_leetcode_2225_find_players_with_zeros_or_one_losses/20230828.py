matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]       # Output: [[1,2,10],[4,5,7,8]]
matches = [[2,3],[1,3],[5,4],[6,4]]                                             # Output: [[1,2,5,6],[]]
matches = [[1,100000]]                                                          # 



with open(r"C:\Users\vito\Desktop\leetcode_0828.txt", 'r') as file:
    content = file.read()
matches = eval(content)

class Solution:
    def findWinners(self, matches):
        win_list = []
        los_list = []

        for match in matches:
            win_list.append(match[0])
            los_list.append(match[1])

        ans_list1 = []
        ans_list2 = []

        key_list = list(set(win_list))
        key_set  = set(los_list)

        for num in key_list:
            if num not in key_set:
                ans_list1.append(num)



        los_list.sort()
        for ind, num in enumerate(los_list[1:-1]):                  # ind
            if num != los_list[ind+2] and num != los_list[ind]:
                ans_list2.append(num)
        
        if len(los_list)==1:
            ans_list2.append(los_list[0])

        try:
            if los_list[0]!=los_list[1]:
                ans_list2.append(los_list[0])
        except:
            pass

        try:
            if los_list[-1]!=los_list[-2]:
                ans_list2.append(los_list[-1])
        except:
            pass

        ans_list1.sort()
        ans_list2.sort()

        return [ans_list1, ans_list2]