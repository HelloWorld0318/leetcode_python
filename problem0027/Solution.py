from _ast import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        index = 0

        for i in range(length):
            if nums[i] != val:
                 nums[index] = nums[i]
                 index += 1

        return index