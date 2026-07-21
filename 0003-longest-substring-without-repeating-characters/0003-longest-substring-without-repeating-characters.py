class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

    #brute force solution - time - o(n^2)
        # maximum=0
        # for i in range(len(s)):
        #     substring=[]
        #     for j in range(i,len(s)):
        #         if s[j] not in substring:
        #             substring.append(s[j])
        #             maximum=max(maximum,len(substring))
        #         else:
        #             break
    
        # return maximum

        # l=0
        # maxcount=0
        # for r in range(l,len(s)):
        #     count=0
        #     if s[r]==s[l]:
        #         left=right
        #         count=1
        #     else:
        #         count+=1
        #     maxcount=max(maxcount,count)

        window=set()
        l=0
        maximum=0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            maximum=max(maximum, r-l+1)

        return maximum