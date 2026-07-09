class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        res = []
        for bucket in buckets[len(buckets)-1: 0: -1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res