from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for left, right, seat in bookings:
            ans[left - 1] += seat
            if right < n:
                ans[right] -= seat

        for i in range(1, n):
            ans[i] += ans[i - 1]
        return ans
