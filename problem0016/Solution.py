from _ast import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = None
        minGap = None
        if nums is not None and len(nums) > 2:
            nums = sorted(nums)
            length = len(nums)
            for i in range(length - 1):
                j = i + 1
                k = length - 1
                while j < k:
                    temp = nums[i] + nums[j] + nums[k]
                    if minGap is None or abs(temp - target) < minGap:
                        ans = temp
                        minGap = abs(temp - target)
                    if temp > target:
                        k -= 1
                    else:
                        j += 1
        return ans
