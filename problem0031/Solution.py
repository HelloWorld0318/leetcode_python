from _ast import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is not None and len(nums) > 1:
            length = len(nums)
            index = length - 1

            while index > 0 and nums[index] <= nums[index - 1]:
                index -= 1

            index -= 1

            if index != -1:
                j = length - 1

                while j > index and nums[j] <= nums[index]:
                    j -= 1

                nums[j], nums[index] = nums[index], nums[j]
            self.reverse(nums, index + 1, length - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        if start >= end:
            return

        i = start
        j = end

        while j > i:
            nums[j], nums[i] = nums[i], nums[j]
            j -= 1
            i += 1
