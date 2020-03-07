from _ast import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        if nums is not None and len(nums) >= 4:
            length = len(nums)
            nums = sorted(nums)

            for i in range(length - 3):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                for j in range(i + 1, length - 2):
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    left, right = j + 1, length - 1
                    while left < right:
                        if nums[i] + nums[j] + nums[left] + nums[right] == target:
                            oneAns = [nums[i], nums[j], nums[left], nums[right]]
                            ans.append(oneAns)
                            left += 1
                            right -= 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1
                        elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                            left += 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                        else:
                            right -= 1
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1
        return ans
