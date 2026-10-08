class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, lv = [], 0

        for ch in s:
            if ch == ")":
                lv -= 1

            if lv  >0:
                res.append(ch)
            if ch == "(":
                lv += 1

        return "".join(res)