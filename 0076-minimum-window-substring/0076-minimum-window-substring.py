class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
    # bruteforce sol- o(n^2 * m) spoace O(m)

        # minimum=float('inf')
        # answer=""
        # hashmap={}
        # for ch in t:
        #     hashmap[ch]=hashmap.get(ch,0)+1
        # for i in range(len(s)):
        #     min_string={}
        
        #     for j in range(i,len(s)):
        #         min_string[s[j]]=min_string.get(s[j],0)+1
        #         valid=True
        #         for char in hashmap:
        #             if min_string.get(char,0)<hashmap[char]:
        #                 valid = False
        #                 break

        #         if valid:
        #             if j-i+1 < minimum:
        #                 minimum=j-i+1
        #                 answer=s[i:j+1]
        #             break
        # return answer


    # optimal sol - time -O(n)
        if t=="": return ""
        hashmap, window={}, {}
        
        for ch in t:
            hashmap[ch]=hashmap.get(ch,0)+1
        
        have, need= 0, len(hashmap)
        l=0
        res,resLen= [-1,-1], float('inf')
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            
            if s[r] in hashmap and window[s[r]]== hashmap[s[r]]:
                have+=1
               
                while have==need:
                    if(r-l+1)< resLen:
                        res=[l, r]
                        resLen=r-l+1
                    
                    window[s[l]]-=1
                    if s[l] in hashmap and window[s[l]] < hashmap[s[l]]:
                        have-=1
                    l+=1

        l,r= res
        return s[l:r+1] if resLen!=float('inf') else ""