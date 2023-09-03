lowLimit = 1
highLimit = 10

lowLimit = 5
highLimit = 15

lowLimit = 19
highLimit = 28


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = [0 for _ in range(46)]
        for num in range(lowLimit, highLimit+1):        
            ans[sum([int(element) for element in str(num)])] += 1
        return max(ans)


ans = Solution()
ans.countBalls(lowLimit=lowLimit, highLimit=highLimit)





########################

num = "6777133339"      #"777"



class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if "999" in num:
            return "999"
        elif "888" in num:
            return "888"
        elif "777" in num:
            return "777"
        elif "666" in num:
            return "666"
        elif "555" in num:
            return "555"
        elif "444" in num:
            return "444"
        elif "333" in num:
            return "333"
        elif "222" in num:
            return "222"
        elif "111" in num:
            return "111"
        elif "000" in num:
            return "000"
        else:
            return ""

ans = Solution()
ans.largestGoodInteger(num=num)





########################

from numpy import mean, array, round


count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,291,822,1386,1925,2418,3016,3695,4283,4768,5349,5800,6480,6948,7484,7925,8758,9089,9606,10043,10883,11344,12040,12412,13104,13543,14086,14767,15280,15651,16449,17097,17480,18197,18571,19330,19554,20201,20904,21452,21814,21879,21856,21047,20610,20089,19729,19415,19094,18379,17957,17562,17044,16585,16434,16082,15381,14774,14486,13883,13563,13015,12886,12291,11680,11356,10999,10441,9949,9460,9159,8626,8196,7761,7280,6906,6477,5996,5655,5104,4553,4174,3796,3277,2822,2493,1957,1584,1064,711,238,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



class Solution:
    def sampleStats(self, count) :
        min_value       = min([i for i, j in enumerate(count) if j !=0])
        max_value       = max([i for i, j in enumerate(count) if j !=0])
        mean_value      = sum(array(count)*array([i for i in range(len(count))]))/sum(count)
        mode_value      = count.index(max(count))
        start = 0
        first_value = []
        if sum(count) % 2 == 0:
            for index, num in enumerate(count):
                start += num
                if start >= sum(count)/2:
                    first_value.append(index)
                    print(index)
                if start >= sum(count)/2 + 1:
                    second_value = index
                    print(index)
                    break
            median_value = (min(first_value)+second_value)/2
        elif sum(count) % 2 ==1:
            for index, num in enumerate(count):
                start += num
                if start >= sum(count)/2 + 0.5:
                    only_value = index
                    break
            median_value = only_value
        
        return[min_value, max_value, mean_value, median_value, mode_value]
    
a = Solution()
a.sampleStats(count)