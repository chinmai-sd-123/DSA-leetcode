class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    # BRUTE FORCE time complexity o(n^2)
        # visited= [False]*len(strs)
        # ans=[]
        # for i in range(len(strs)):
        #     if visited[i]:
        #         continue
        #     group=[strs[i]] 
        #     visited[i]=True
        #     for j in range(i+1, len(strs)):
        #         if sorted(strs[i])==sorted(strs[j]):
        #             group.append(strs[j])
        #             visited[j]=True
        #     ans.append(group)
        # return ans


    # hashmap optimal sol time complexity (o(nklogk))
        # hashmap={}
        # for word in strs:
        #     key=tuple(sorted(word))
        #     if key not in hashmap:
        #         hashmap[key]=[word]
        #     else:
        #         hashmap[key].append(word)
        # return list(hashmap.values())

    # better pythonic way using defaultdict
        from collections import defaultdict
        hashmap=defaultdict(list)
        for word in strs:
            key=tuple(sorted(word))
            hashmap[key].append(word)
        return list(hashmap.values())