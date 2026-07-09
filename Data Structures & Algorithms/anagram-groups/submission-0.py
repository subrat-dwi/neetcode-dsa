class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st_count = defaultdict(list)
        for st in strs:
            st_count["".join(sorted(st))].append(st)

        return list(st_count.values())