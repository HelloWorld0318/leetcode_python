from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        ans.append(0)
        if n > 0:
            for i in range(n):
                heightest = 1 << i
                length = len(ans)
                for j in range(length - 1, -1, -1):
                    ans.append(ans[j] | heightest)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.grayCode(3))
