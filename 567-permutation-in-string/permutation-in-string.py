class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        map1={}

        map2={}

        for i in s1:

            map1[i] = map1.get(i,0)+1

        l,r,maxfreq=0,0,0

        while(r!=len(s2)):


            map2[s2[r]] = map2.get(s2[r],0)+1

           

            while ((r-l+1) > len(s1)):

                map2[s2[l]]=map2.get(s2[l])-1

                if map2.get(s2[l])==0:
                    map2.pop(s2[l])

                l+=1
            

            if map1==map2:
                return True

            r+=1

        return False
        