class Solution:
    def minWindow(self, s: str, t: str) -> str:

        map1={}
        map2={}

        for i in t:
            map1[i] = map1.get(i,0)+1

        ans=[-1,0,0]

        formed=0
        l=0
        r=0

        while(r!=len(s)):

            map2[s[r]] = map2.get(s[r],0)+1

            if s[r] in t and map1[s[r]]==map2[s[r]]:
                formed+=1

            while(formed == len(map1)):

                window_size = r-l+1

                if ans[0]==-1 or window_size < ans[0]:

                    ans[0]=window_size
                    ans[1]=l
                    ans[2]=r

                if s[l] in t and map1[s[l]]==map2[s[l]]:

                    formed-=1

                map2[s[l]] = map2.get(s[l],0)-1

                if map2[s[l]]==0:
                    del map2[s[l]]

                l+=1

            r+=1
        return "" if ans[0]==-1 else s[ans[1]:ans[2]+1]



        