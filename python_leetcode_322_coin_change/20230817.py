coins = [1,2,10] ; amount = 11      # 3
coins = [2] ; amount = 3            # -1
coins = [186,419,83,408] ; amount = 6249


import random        


# def give_an_answer(coins, amount):
#     key_value = amount
#     ans = 0
#     while key_value>=min(coins):
#         ran = random.choice(coins)
#         print(ran)
#         ans += key_value//ran
#         key_value = key_value%ran
#         coins = [coin for coin in coins if coin<=key_value]
#         if coins==[] and key_value==0:
#             return ans      # print(ans) 
#         elif coins==[]:
#             break
#     return -1               # print(-1)


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0        
        if min(coins)>amount:
            return -1

        # coins = list(set(coins))
        # coins = sorted(coins, reverse=True)
        # coins = [coin for coin in coins if coin<=amount]    # adjusted
        # key_list = []
        # for _ in range(1000):
        #     key_list.append(give_an_answer(coins, amount))
        # if max(key_list)==-1:
        #     return -1
        # else:
        #     return min([num for num in key_list if num>-1])
        
        dp          = [False] * (amount + 1)
        dp[0]       = True
        key_list    = [9999999999] * (amount+1)
        key_list[0] = 0

        for coin in coins:
            print(coin)
            for i in range(coin, amount + 1):
                dp[i] |= dp[i - coin]
                if dp[i] == True:
                    key_list[i] = key_list[i-coin]+1 if key_list[i-coin]+1<key_list[i] else key_list[i]
                    print(coin,i)
        if dp[amount]==True:
            return key_list[amount]
        else:
            return -1


ans = Solution()
ans.coinChange(amount=amount, coins=coins)



















def can_pay_exact_amount(amount, denominations):
    dp          = [False] * (amount + 1)
    dp[0]       = True
    key_list    = [99999] * (amount+1)
    key_list[0] = 0

    for denom in denominations:
        print(denom)
        for i in range(denom, amount + 1):
            dp[i] |= dp[i - denom]
            if dp[i] == True:
                key_list[i] = key_list[i-denom]+1 if key_list[i-denom]+1<key_list[i] else key_list[i]
                print(denom,i)
    if dp[amount]==True:
        return key_list[amount]
    return False

denominations = [83, 186, 408, 419]
amount = 6249

if can_pay_exact_amount(amount, denominations):
    print("可以剛好支付", amount, "元")
else:
    print("無法剛好支付", amount, "元")