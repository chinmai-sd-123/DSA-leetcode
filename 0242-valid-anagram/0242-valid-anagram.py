class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    # brute force time complexity o(n^2)
        # if len(s)!=len(t):
        #     return False
        # for i in range(len(s)):
        #     count_s=0
        #     count_t=0
        #     for j in range(len(s)):
        #         if s[i]==s[j]:
        #             count_s+=1
        #         if s[i]==t[j]:
        #             count_t+=1
        #     if count_s!=count_t:
        #         return False
        # return True



    # python built in frequency time complexity o(n)
        # from collections import Counter 
        # n=Counter(s)
        # y=Counter(t)
        # if n==y:
        #     return True
        # return False


    # sorting technique    
        # if len(s)!=len(t):
        #     return False
        # sorted_s=sorted(s)
        # sorted_t=sorted(t)
        # for i in range(len(s)):
        #     if sorted_s[i]!=sorted_t[i]:
        #         return False
        # return True\


    # hashmap    
        hashmap={}

        for ch in s:
            
            hashmap[ch]=hashmap.get(ch,0)+1
        for ch in t:
            hashmap[ch]=hashmap.get(ch,0)-1
        for value in hashmap.values():
            if value!=0:
                return False
        return True
