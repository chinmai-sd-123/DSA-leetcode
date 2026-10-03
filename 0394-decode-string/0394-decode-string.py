class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # brute force , will check the content from innnermost bracket

        # while '[' in s:
        #     end= s.find(']')
        #     start= s.rfind('[',0,end)
        #     content= s[start +1:end]
        #     i=start-1
        #     while i>=0 and s[i].isdigit():
        #         i-=1
        #     num= int(s[i+1:start])
        #     decoded=num*content
        #     s= s[:i+1]+decoded+s[end+1:]
        # return s

        # optimal using stack- o(n)

        stack= []
        current_number= 0
        current_string=""
        for ch in s:
            if ch.isdigit():
                current_number= current_number*10+ int(ch)
            elif ch =='[':
                stack.append((current_number, current_string))
                current_string=""
                current_number=0
            elif ch.isalpha():
                current_string+=ch
            elif ch=="]":
                num, previous_string= stack.pop()
                current_string=previous_string+current_string*num
        return current_string