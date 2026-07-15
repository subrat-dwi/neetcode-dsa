class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)
        maxi = 0
        freq = {}
        max_freq = 0
        left = 0

        for right in range(l):
            f = freq.get(s[right], 0) + 1
            freq[s[right]] = f

            max_freq = max(f, max_freq)

            if (right-left+1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            right += 1
            maxi = max(maxi, right-left)

        return maxi