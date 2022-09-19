from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, next_visits: List[int]) -> int:
        n = len(next_visits)
        dp = [0] * n
        MODULO = 10**9 + 7
        for i in range(n - 1):
            dp[i + 1] = (2 * dp[i] + 2 - dp[next_visits[i]]) % MODULO
        return dp[n - 1]
