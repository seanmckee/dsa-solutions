class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        s_string = "".join(sorted_s)
        t_string = "".join(sorted_t)
        if s_string == t_string:
            return True
        return False