class Solution:
    def minWindow(self, s: str, t: str) -> str:


        map1= {}
        map2={}

        for i in t:

            map1[i] = map1.get(i,0)+1

        formed=0
        l=0
        r=0

        window = [-1,-1,-1]

        while(r!=len(s)):

            map2[s[r]]= map2.get(s[r],0)+1

            if s[r] in t and map1[s[r]]==map2[s[r]]:
                formed+=1

            while formed == len(map1):

                if window[0]==-1 or window[0]>(r-l)+1:

                    window[0]=r-l+1
                    window[1]=l
                    window[2]=r

                

                if s[l] in t and map2[s[l]]==map1[s[l]]:

                    formed-=1
                map2[s[l]]-=1

                    
                l+=1

                

            r+=1
            


        return "" if window[0]==-1 else s[window[1]:window[2]+1]


                 




        