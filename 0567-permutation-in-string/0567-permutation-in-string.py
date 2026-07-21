class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
    # brute force sol- o(n^2)
        # freq_s1= {}
        # for ch in s1:
        #     freq_s1[ch]=freq_s1.get(ch,0)+1
        
        # for i in range(len(s2)-len(s1)+1):
        #     freq_s2={}
        #     for j in range(i,len(s1)+i):
        #         freq_s2[s2[j]]=freq_s2.get(s2[j],0)+1
            
        #     if freq_s1==freq_s2:
        #         return True
        # return False

    # sliding window - time- o(n) and space- O(1)

        freq_s1={}
        freq_s2={}
        for ch in s1:
            freq_s1[ch]=freq_s1.get(ch,0)+1
        
        if len(s1)>len(s2):
            return False
        for i in range(0,len(s1)):
            freq_s2[s2[i]]=freq_s2.get(s2[i],0)+1
        
        if freq_s1==freq_s2:
            return True
        l=0
        for r in range(len(s1),len(s2)):
            freq_s2[s2[l]]-=1
            if freq_s2[s2[l]]==0:
                freq_s2.pop(s2[l])
            freq_s2[s2[r]]=freq_s2.get(s2[r],0)+1
            l+=1
            if freq_s1==freq_s2:
                return True
        return False

