from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            value = (digits[i] + carry) % 10
            carry = 1 if digits[i] + carry >= 10 else 0
            digits[i] = value
            if carry == 0:
                break

        if carry == 1:
            digits.insert(0,1)
        return digits