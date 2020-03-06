from _ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            medium = (start + end) >> 1;
            if nums[medium] == target:
                return medium

            if nums[start] <= nums[medium]:
                if nums[start] <= target and target < nums[medium]:
                    end = medium - 1
                else:
                    start = medium + 1
            else:
                if nums[medium] < target and target <= nums[end]:
                    start = medium + 1
                else:
                    end = medium - 1
        return -1
