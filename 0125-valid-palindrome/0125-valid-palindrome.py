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



         # two pointers with time complexity - o(n) space -o(n)
        # clean=[]
        # for ch in  s:
        #     if ch.isalnum():
        #         clean.append(ch)

        # clean_s="".join(clean).lower()
        
        # left=0
        # right= len(clean_s)-1
        # while left<right:
        #     if clean_s[left]!=clean_s[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True

    # two pointers with space o (1)
        # left=0
        # right=len(s)-1
        # while left<right:
        #     if not s[left].isalnum():
        #         left+=1
        #     elif not s[right].isalnum():
        #         right-=1
        #     elif  s[left].lower()!=s[right].lower():
        #         return False
        #     else:
        #         left+=1
        #         right-=1
        # return True