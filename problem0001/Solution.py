from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value2Index = {}
        for i in range(len(nums)):
            if target - nums[i] in value2Index:
                return [value2Index[target - nums[i]], i]
            value2Index[nums[i]] = i
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    ans = solution.twoSum(nums, target)
    print(ans)
