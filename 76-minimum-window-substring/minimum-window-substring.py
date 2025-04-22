class Solution:
    def minWindow(self, s: str, t: str) -> str:

        map1={}
        map2={}

        for i in t:

            map1[i] = map1.get(i,0)+1

        formed=0

        output=[-1,0,0]

        l,r=0,0

        while(r!=len(s)):

            map2[s[r]] = map2.get(s[r],0)+1

            if s[r] in t and map1[s[r]]==map2[s[r]]:
                formed+=1

            while formed == len(map1):

                windowsize = r-l+1

                if output[0]== -1 or output[0]>windowsize:

                    output[0]=windowsize

                    output[1]=l
                    output[2]=r

                if s[l] in t and map1[s[l]]==map2[s[l]]:

                    formed-=1

                map2[s[l]]-=1

                if map2[s[l]]==0:
                    del map2[s[l]]

                l+=1

                

            r+=1

        return "" if output[0]==-1 else s[output[1]:output[2]+1]





        