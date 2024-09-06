class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        longestSubstring = 1

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        charSet = set()
        charSet.add(s[l])
        currentSubstring = 1
        while r < len(s):
            if s[r] not in charSet:
                currentSubstring += 1
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                currentSubstring = r - l + 1

            charSet.add(s[r])
            longestSubstring = max(longestSubstring, currentSubstring)
            r += 1
        return longestSubstring
