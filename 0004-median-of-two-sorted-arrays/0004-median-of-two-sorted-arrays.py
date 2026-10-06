class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        # i=0
        # j=0
        # n=len(nums1)
        # m=len(nums2)
        # res=[]
        # while(i<n and j<m):
        #     if nums1[i]<=nums2[j]:
        #         res.append(nums1[i])
        #         i+=1
        #     else:
        #         res.append(nums2[j])
        #         j+=1
        # while i<n:
        #     res.append(nums1[i])
        #     i+=1
        # while j<m:
        #     res.append(nums2[j])
        #     j+=1
        # if len(res)%2==0:
        #     res1=res[len(res)//2]
        #     res2=res[len(res)//2-1]
        #     return (res1+res2)/2
        # else:
        #     return res[len(res)//2]

     

        # Binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        half = (m + n + 1) // 2

        while low <= high:

            partition1 = (low + high) // 2
            partition2 = half - partition1

            # Boundary values of nums1
            if partition1 == 0:
                left1 = float("-inf")
            else:
                left1 = nums1[partition1 - 1]

            if partition1 == m:
                right1 = float("inf")
            else:
                right1 = nums1[partition1]

            # Boundary values of nums2
            if partition2 == 0:
                left2 = float("-inf")
            else:
                left2 = nums2[partition2 - 1]

            if partition2 == n:
                right2 = float("inf")
            else:
                right2 = nums2[partition2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2

            # Partition1 is too far right
            elif left1 > right2:
                high = partition1 - 1

            # Partition1 is too far left
            else:
                low = partition1 + 1