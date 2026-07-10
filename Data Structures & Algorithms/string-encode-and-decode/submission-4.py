class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            l = len(strs[i])
            strs[i] = f"{l:03d}{strs[i]}"
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        lock = False
        l = 0
        i = 0

        strs = []
        while i < len(s):
            if not lock:
                prefix = s[i:i+3]
                l = int(prefix)
                lock = True
                i = i+3
                if i == len(s):
                    strs.append("")

            else:
                strs.append(s[i:i+l])
                i = i+l
                lock = False

            
        return strs