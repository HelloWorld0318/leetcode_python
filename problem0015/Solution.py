from _ast import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if nums is not None and len(nums) >= 3:
            nums = sorted(nums)
            length = len(nums)
            target = 0
            for i in (range(length - 2)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                j = i + 1
                k = length - 1

                while j < k:
                    if nums[i] + nums[j] + nums[k] == target:
                        oneResult = [nums[i], nums[j], nums[k]]
                        ans.append(oneResult)
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif nums[i] + nums[j] + nums[k] < target:
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                    else:
                        k -= 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1

        return ans

