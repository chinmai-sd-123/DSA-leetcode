class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #store the max_length\
        # max_length=0
        
        # for i in range(len(s)):
            
        #     seen=set()
        #     seen=({s[i]})
        #     length=1
        #     for j in range(i+1,len(s)):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         length+=1
        #     max_length=max(length, max_length)

        # return max_length

        # optimal

        l=0
        max_length=0
        seen=set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            max_length=max(max_length, r-l+1)
        return max_length