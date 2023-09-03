from scipy.stats import rankdata

nums = [432,43243]
nums = [34323,3432]
nums = [0,0]


nums2 = nums.copy()

ans_list = []
for f in range(3):                  # f=0

    largest_length = len(str(max(nums)))

    for index, num in enumerate(nums):
        if len(str(num))<largest_length:
            if f != 2:
                nums[index] = int(str(num)+str(num)[-f]*(largest_length-len(str(num))))
            else:
                nums[index] = int(str(num)+str(9)*(largest_length-len(str(num))))

    index_want = []
    for j in range(len(nums)):
        for index, rank in enumerate(list((len(nums)-1)-(rankdata(nums)-1))):
            if int(rank) == j:
                index_want.append(index)
        j += 1

    ans = ''
    for k in index_want:
        ans += str(nums2[k])
    ans_list.append(ans)
    nums = nums2
    nums2 = nums.copy()

max(ans_list) if int(max(ans_list))!=0 else 0


