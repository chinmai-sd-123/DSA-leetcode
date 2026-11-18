from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq_s1=Counter(s1)
        # if len(s1)>len(s2):
        #     return False
        # for i in range(len(s2)-len(s1)+1):
        #     freq={}
        #     for j in range(i, i+len(s1)):
        #         freq[s2[j]]=freq.get(s2[j],0)+1
           
        #     if freq_s1==freq:
        #         return True
        # return False

        # optimal sol
        n = len(s1)

        if n > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # Build initial window
        for i in range(n):
            freq1[ord(s1[i])-ord('a')]+=1
            freq2[ord(s2[i])-ord('a')]+=1
        
        # Compare frequencies
        if freq1==freq2:
            return True
        # Slide window through s2
        for i in range(n, len(s2)):
            # Remove outgoing character
            left = ord(s2[i-n]) - ord('a')
            right = ord(s2[i]) - ord('a')

            freq2[left] -= 1
            freq2[right] += 1
            # Add incoming character
            if freq2==freq1:
                return True
            # Compare frequencies

        return False


        