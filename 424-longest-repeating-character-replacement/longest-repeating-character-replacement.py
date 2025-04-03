class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        map = {}

        l=0
        r=0
        maxfreq=0

        ans=0

        while(r!=len(s)):

            map[s[r]] = map.get(s[r],0)+1

            maxfreq= max(maxfreq,map[s[r]])


            while( (r-l+1)-maxfreq>k):

                map[s[l]] = map.get(s[l])-1

                l+=1

            

            ans = max(ans,(r-l+1))

            r+=1

        return ans
        