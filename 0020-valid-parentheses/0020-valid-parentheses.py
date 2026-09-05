class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        # while "{}" in s or "[]" in s or "()" in s:
        #     s=s.replace("{}","")
        #     s=s.replace("[]","")
        #     s=s.replace("()","")
        # return s==""

        # optimal O(n)
        x=[]
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for ch in s:
            if ch in "({[":
                x.append(ch)
            else:
                if not x or x[-1]!=pairs[ch]:
                    return False
                x.pop()

        return len(x)==0