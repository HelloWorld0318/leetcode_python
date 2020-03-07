class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        dic = {}
        start = -1
        ans = 0

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] > start:
                start = dic[s[i]]
            dic[s[i]] = i
            ans = max(ans, i - start)
        return ans
