class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
    # brute force sol-o(n*m) space =O(m)

        # res=[]
        # hashmap={}
        # for ch in p:
        #     hashmap[ch]=hashmap.get(ch,0) + 1
        # for i in range(len(s)-len(p)+1):
        #     window= {}
        #     for j in range(i,i+len(p)):
        #         ele=s[j]
        #         window[ele]= window.get(ele,0)+1
        #     if window==hashmap:
        #         res.append(i)
        # return res

    # optimal solution using sliding window- O(n) and space- O(m)
        res=[]
        hashmap={}
        for ch in p:
            hashmap[ch]=hashmap.get(ch,0) + 1
        l=0
        window={}

        if len(s) <len(p): return []
        for r in range(len(s)):
            ele=s[r]
            window[ele]= window.get(ele,0)+1

            if r-l+1> len(p):
                window[s[l]]-=1
                if window[s[l]]==0:
                    del window[s[l]]
                l+=1

            if window==hashmap:
                res.append(l)
                
        return res
    



