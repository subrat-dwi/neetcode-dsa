class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        left, right = 0, 0
        last_seen = {}
        maxi = 0

        for i in range(l):
            if s[i] in last_seen:
                ls_id = last_seen[s[i]]
                if ls_id >= left:
                    left = ls_id + 1
                last_seen[s[i]] = i

            else:
                last_seen[s[i]] = i

            right += 1
            maxi = max(right-left, maxi)
        
        return maxi

