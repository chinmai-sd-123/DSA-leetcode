class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right= 0, len(s)-1
        while left< right:
            while left < right and not self.isalphaNum(s[left]):
                left+=1
            while right > left and not self.isalphaNum(s[right]):
                right-=1

            if s[left].lower()!=s[right].lower():
                return False
            left, right = left+1, right -1
        return True
    
    def isalphaNum(self, c):
        return (ord('A') <= ord(c) <=ord('Z') or
                ord('a') <= ord(c) <=ord('z') or
                ord('0') <= ord(c) <=ord('9'))