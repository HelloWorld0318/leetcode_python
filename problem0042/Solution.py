from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        if height is None or len(height) <= 2:
            return ans
        length = len(height)

        leftHeight = height[0]
        rightHeight = height[length - 1]

        left = [0]
        right = [0]

        for i in range(1, length):
            left.append(leftHeight)
            if leftHeight < height[i]:
                leftHeight = height[i]

        for i in range(length - 2, -1, -1):
            right.append(rightHeight)
            if rightHeight < height[i]:
                rightHeight = height[i]

        right = right[::-1]

        for i in range(length):
            low = min(left[i], right[i])
            if height[i] < low:
                ans += low - height[i]

        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans = solution.trap(nums)
    print(ans)
