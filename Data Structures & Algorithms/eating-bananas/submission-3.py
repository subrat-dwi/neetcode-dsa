class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        l, r = 1, m+1
        min_r = m

        while l < r:
            mid = (l + r)//2
            hours = 0

            for p in piles:
                hours += -(-p//mid)
            
            if hours <= h:
                min_r = mid
                r = mid
            else:
                l = mid+1
        return min_r

