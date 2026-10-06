class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        i=0
        j=0
        n=len(nums1)
        m=len(nums2)
        res=[]
        while(i<n and j<m):
            if nums1[i]<=nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i<n:
            res.append(nums1[i])
            i+=1
        while j<m:
            res.append(nums2[j])
            j+=1
        if len(res)%2==0:
            res1=res[len(res)//2]
            res2=res[len(res)//2-1]
            return (res1+res2)/2
        else:
            return res[len(res)//2]
