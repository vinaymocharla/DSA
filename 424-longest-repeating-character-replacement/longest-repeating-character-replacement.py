class Solution:
    def characterReplacement(self, s: str, k: int) -> int:



        

        freq = {}

        l=0
        r=0

        ans=0

      

        while(r!=len(s)):


            freq[s[r]]= freq.get(s[r],0)+1


            maxfreq = max(freq.values())
            

            while((r-l+1)- maxfreq>k):

                
                freq[s[l]] = freq.get(s[l])-1


                

                l+=1
                

            ans = max(ans,(r-l+1))

            r+=1

        return ans

            







            


        