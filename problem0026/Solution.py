from _ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        index = 0

        for i in range(len(nums)):
            if nums[index] != nums[i]:
                index = index + 1
                nums[index] = nums[i]
        return index + 1