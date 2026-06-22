class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "[": "]", "{": "}"}
        res = []

        for c in s:
            if c in pairs:                 # opening bracket → push
                res.append(c)
            else:                          # closing bracket → must match top
                if not res:                # nothing to close
                    return False
                last_added = res.pop()
                if pairs[last_added] != c:  # wrong type of closer
                    return False

        return len(res) == 0               # leftover openers → invalid
        