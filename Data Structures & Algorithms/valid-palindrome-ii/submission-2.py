class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            start, end = 0, len(s)-1
            while(start < end):
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        start, end = 0, len(s)-1
        charDeleted = False
        while start < end:
            if s[start] != s[end] and not charDeleted:
                if isPalindrome(s[start+1:end+1]):
                    start += 1
                    charDeleted = True
                    continue
                elif isPalindrome(s[start:end]):
                    end -= 1
                    charDeleted = True
                    continue
                else: 
                    return False
                
            if s[start] != s[end]: return False
            start += 1
            end -= 1
        return True

                