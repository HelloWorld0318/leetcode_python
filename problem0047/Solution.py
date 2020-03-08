from _ast import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if nums is not None and len(nums) > 0:
            self.dfs(nums, 0, ans)
        return ans

    def dfs(self, nums: List[int], index: int, ans: List[int]) -> None:
        if index >= len(nums):
            oneAns = []
            for i in range(len(nums)):
                oneAns.append(nums[i])
            ans.append(oneAns)
            return

        for i in range(index, len(nums)):
            # nums[index]和nums[i-1]中有与nums[i]相同的元素，那么就不进行交换
            if self.seen(nums, index, i):
                continue
            self.swap(nums, index, i)
            self.dfs(nums, index + 1, ans)
            self.swap(nums, index, i)

    def seen(self, nums: List[int], start: int, end: int) -> bool:
        if start < end:
            for i in range(start, end):
                if nums[i] == nums[end]:
                    return True
        return False

    def swap(self, nums: List[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]
