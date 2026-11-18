class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # max_l=0
        # for i in range(len(s)):
        #     freq={}
        #     max_freq=0
        #     for j in range(i, len(s)):
        #         window= j-i+1
        #         freq[s[j]]=freq.get(s[j],0)+1
        #         max_freq= max(max_freq, freq[s[j]])

        #             max_l=max(max_l, window)

        # return max_l

        l=0
        max_l=0
        max_freq=0
        freq=[0]*26
        for r in range(len(s)):
            idx=ord(s[r])-ord("A")
            freq[idx]+=1
            max_freq=max(max_freq, freq[idx])
            while (r-l+1)-max_freq>k:
                left_index=ord(s[l])-ord("A")
                freq[left_index]-=1
                l+=1
            max_l=max(max_l, r-l+1)
        return max_l

