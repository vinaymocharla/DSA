class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqmap = {}

        maxval,ans = 0,0

        l=0
        r=0

        while(r!=len(s)):

            freqmap[s[r]] = freqmap.get(s[r],0)+1

            maxval = max(maxval,freqmap.get(s[r]))


            while((r-l+1)-maxval >k):

                freqmap[s[l]] = freqmap.get(s[l])-1

                l+=1

            ans = max(ans,(r-l+1))

            r+=1

        return ans

        