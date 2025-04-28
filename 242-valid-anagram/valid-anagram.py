class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map1={}


        for i in s:
            map1[i] = map1.get(i,0)+1
        
        for j in t:
            if j in map1:
                map1[j]-=1
                if map1[j]==0:
                    del map1[j]
            else:
                return False
        return len(map1) ==0

        