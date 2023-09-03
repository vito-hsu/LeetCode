changed = [1,3,4,2,6,8]     # [1,3,4]
changed = [6,3,0,1]         # []
changed = [1]               # []
changed = [0,0,0,0]         # [0,0]
changed = [2,1,2,4,2,4]     # [1,2,2]
changed = [1,1,1,1,1,1]
changed = [2,1,2,4,2,4]*20000

##
with open(r"C:\Users\vito\Desktop\leetcode_0816-3.txt", 'r') as file:
    content = file.read()

try:
    your_list = eval(content)
except SyntaxError:
    print("文件内容不是有效的列表表示")
    your_list = []

print(your_list)
changed = your_list
##

class Solution:
    def findOriginalArray(self, changed):
        if (len(changed)<=1) or (len(changed)%2!=0) or (changed.count(0)%2!=0) or min(changed)>50000:             
            print('[e0]')                     #return []

        ans_list = []
        changed = sorted(changed)
        zero_num = changed.count(0)
        ans_list.extend([0]*int(zero_num/2))
        del changed[:zero_num]

        changed1 = [x for x in changed if x <= 50000]
        changed2 = [x for x in changed if x > 50000]

        i = 0
        while len(changed1)>0 or len(changed2)>0:
            print(i) ; i += 1
            first_value = changed1[0]

            if first_value<25001:
                try:
                    ans_list.append(first_value) ; changed1.remove(first_value) ; changed1.remove(first_value*2)
                except:
                    print('[e1]')                 #return []
            else:
                try:
                    ans_list.append(first_value) ; changed1.remove(first_value) ; changed2.remove(first_value*2)
                except:
                    print('[e2]')                 #return []
        return ans_list

from time import time 
start1 = time()
ans = Solution()
final_ans = ans.findOriginalArray(changed=changed)
end1 = time()
end1 - start1

# class Solution:
#     def findOriginalArray(self, changed):
#         if (len(changed)<=1) or (len(changed)%2!=0):
#             return []               # print("[0]")    
        
#         ans_list = []
#         key_list = []

#         ####### for test cases changed = [0,0,0,0]   ######
#         if changed.count(0)%2!=0:
#             return []
        
#         while 0 in changed:
#             changed.remove(0)
#             changed.remove(0)
#             ans_list.append(0)
#         ###################################################

#         changed = sorted(changed)

        
#         for num in changed:
#             if (num%2!=0) and (num*2 in changed):
#                 ans_list.append(num)
#                 key_list.append(num*2)
#             elif (num%2!=0) and (num*2 not in changed):
#                 return []           # print("[1]")
#             elif (num%2==0) and (num/2 not in ans_list) and (num*2 in changed):
#                 ans_list.append(num)
#                 key_list.append(num*2)
#             elif (num%2==0) and (num in key_list):
#                 continue
#             elif (num%2==0) and (num/2 not in key_list) and (num*2 not in changed):
#                 return []           # print('[2]')
            
#         return ans_list



import time 
start1 = time.time()
a = 0
while a<300000000:
    a = a + 1
a
end1 = time.time()

start2 = time.time()
a = 0
for _ in range(300000000):
    a = a + 1
a
end2 = time.time()

end1-start1
end2-start2






list1 = [num for num in range(1000000)]
list2 = [num for num in range(5478, 9653)]
ans1 = [num for num in list1 if num not in list2]

key_set = set(list2)
ans2 = [num for num in list1 if num not in key_set]

ans1 == ans2





list1 = [num for num in range(10000000)]
for num in list1:
    list1.remove(num)

list2 = []
for num in list1:
    list2.append(num)





start3 = time()
list1 = [num for num in range(10000000)]
list3 = [num for num in range(5000, 6550)]
for num in list3:
    list1.remove(num)
end3 = time()


start4 = time()
list4 = [num for num in range(100000)]
list3 = [num for num in range(6550)]
for num in list3:
    list4.remove(num)
end4 = time()

end3-start3
end4-start4



