class Solution {
    public int scoreOfString(String s) {
        int sum=0;

        for(int i =0;i<s.length()-1;i++){


            int ch1 = (int)s.charAt(i);
            int ch2 = (int)s.charAt(i+1);

            sum+= Math.abs(ch2-ch1);











        }
        return sum;
        
    }
}