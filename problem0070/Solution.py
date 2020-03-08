class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        f1 = 1
        f2 = 2

        while n > 2:
            f2, f1 = f1 + f2, f2
            n -= 1

        return f2


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(4))
