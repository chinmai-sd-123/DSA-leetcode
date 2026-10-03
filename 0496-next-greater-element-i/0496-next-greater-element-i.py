class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ans=[-1]*len(nums1)
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums2[j]==nums1[i]:
        #             for k in range(j+1,len(nums2)):
        #                 if nums2[k]>nums1[i]:
        #                     ans[i]=nums2[k]
        #                     break
        #             break

        
        # return ans

        # better than above
        # o(m*n)
        # nums1index={ n:i for i, n in enumerate(nums1)}
        # res= [-1]*len(nums1)
        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1index:
        #         continue
        #     for j in range(i+1,len(nums2)):
        #         if nums2[j]>nums2[i]:
        #             idx=nums1index[nums2[i]]
        #             res[idx]=nums2[j]
        #             break

        # return res

        # optimal sol with o(n+m):

        
        nums1index={ n:i for i, n in enumerate(nums1)}
        res= [-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur> stack[-1]:
                val= stack.pop()
                idx= nums1index[val]
                res[idx]=cur
            if cur in nums1index:
                stack.append(cur)
        return res