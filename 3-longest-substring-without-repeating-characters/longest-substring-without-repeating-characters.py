class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        stringset = set()

        ans=0

        l=0
        r=0

        while(r!=len(s)):

            while s[r] in stringset:

                stringset.remove(s[l])
                l+=1

            
            stringset.add(s[r])

            ans = max(ans,r-l+1)

            r+=1

        return ans
        