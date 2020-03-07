from _ast import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        if len(nums) <= 1:
            return len(nums)

        map = {}
        for num in nums:
            map[num] = 1

        ans = 0

        for num in nums:
            if num in map:
                length = 1

                left = num - 1
                right = num + 1

                while left in map:
                    del map[left]
                    length += 1
                    left -= 1

                while right in map:
                    del map[right]
                    length += 1
                    right += 1

                if ans < length:
                    ans = length

        return ans