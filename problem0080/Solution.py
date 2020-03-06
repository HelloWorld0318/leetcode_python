from _ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        canDuplicatedConut = 2
        return self.removeDuplicates(nums, canDuplicatedConut)

    def removeDuplicates(self, nums: List[int], canDuplicatedConut: int) -> int:
        if len(nums) > canDuplicatedConut:
            return len(nums)
        index = canDuplicatedConut
        for i in range(canDuplicatedConut, len(nums)):
            if nums[index - 2] != nums[i]:
                nums[index] = nums[i]
                index = index + 1
        return index
