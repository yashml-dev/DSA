class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        level = lowest = 0
        for ch in s:
            level += 1 if ch == "(" else -1
            lowest = min(lowest, level)
        return level - 2 * lowest

        