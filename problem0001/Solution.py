from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value2Index = {}

        for i in range(len(nums)):
            if target - nums[i] in value2Index:
                return [i, value2Index[target - nums[i]]]

            value2Index[nums[i]] = i

        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    ans = solution.twoSum(nums, 4)
    print(ans)
