from _ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.findKthSortedArrays(nums1, 0, nums2, 0, length // 2) +
                    self.findKthSortedArrays(nums1, 0, nums2, 0, length // 2 + 1)) / 2
        else:
            return self.findKthSortedArrays(nums1, 0, nums2, 0, length // 2 + 1)

    def findKthSortedArrays(self, nums1: List[int], index1: int, nums2: List[int], index2: int, kth: int):
        if len(nums1) == index1:
            return nums2[index2 + kth - 1]
        elif len(nums2) == index2:
            return nums1[index1 + kth - 1]

        if kth == 1:
            return min(nums1[index1], nums2[index2])

        nums1Value = nums1[index1 + kth // 2 - 1] if index1 + kth // 2 - 1 < len(nums1) else None
        nums2Value = nums2[index2 + kth // 2 - 1] if index2 + kth // 2 - 1 < len(nums2) else None

        if nums2Value is None or (nums1Value is not None and nums1Value < nums2Value):
            return self.findKthSortedArrays(nums1, index1 + kth // 2, nums2, index2, kth - kth // 2)
        else:
            return self.findKthSortedArrays(nums1, index1, nums2, index2 + kth // 2, kth - kth // 2)
