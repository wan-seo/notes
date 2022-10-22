class Solution:
    def countEven(self, num: int) -> int:
        def digitSum(number):
            return sum(map(int, list(str(number))))
        count = 0
        for i in range(1, num + 1):
            if digitSum(i) % 2 == 0:
                print(digitSum(i))
                count += 1
        return count

s = Solution()
ans = s.countEven(4)
print(ans)