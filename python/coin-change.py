from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX_VAL = 10001
        arr = [MAX_VAL] * (amount + 1)
        arr[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                if arr[i-coin] != MAX_VAL:
                    arr[i] = min(arr[i], arr[i-coin] + 1)

        if arr[amount] == MAX_VAL:
            return -1

        return arr[amount]


if __name__ == '__main__':
    # test values
    coins = [1, 2, 5]
    amount = 11
    solution = Solution()
    print(solution.coinChange(coins=coins, amount=amount))
