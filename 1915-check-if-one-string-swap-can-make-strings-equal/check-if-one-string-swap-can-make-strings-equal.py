class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        i=-1
        j=-1
        cnt=0

        for k in range(len(s1)):

            if s1[k]!=s2[k]:
                cnt+=1

                if i==-1:i=k
                elif j==-1:j=k

        if cnt==0: return True
        elif cnt==2 and s1[i]==s2[j] and s1[j]==s2[i] :return True
        else: return False

        
        