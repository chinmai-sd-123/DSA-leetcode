class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
    # brute force sol- time - o(n^2)
       
        # maximum=0
        # for i in range(len(s)):
        #     hashmap={}
        #     for j in range(i,len(s)):
        #         hashmap[s[j]]=hashmap.get(s[j],0)+1

        #         length=j-i+1
        #         maxFreq=max(hashmap.values())
        #         replacements=length-maxFreq

        #         if replacements <=k:
        #             maximum=max(maximum, length)
        #         else:
        #             break
        # return maximum
        
    #optimal using sliding window- o(n)
        l=0
        maximum=0
        hashmap={}
        maxFreq=0
        for r in range(len(s)):
            hashmap[s[r]]=hashmap.get(s[r],0)+1
    
            maxFreq=max(maxFreq, hashmap[s[r]])
            

            while (r-l+1)- maxFreq>k:
                hashmap[s[l]]=hashmap.get(s[l],0)-1
                l+=1
            maximum=max(maximum,r-l+1)
        return maximum