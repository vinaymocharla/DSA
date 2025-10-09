class Solution {
    public int romanToInt(String s) {

        Map<Character,Integer> map = new HashMap<>();

        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);

        char[] ch = s.toCharArray();
        int sum=0;

        for(int i=0;i<=ch.length-2;i++){

            int current = map.get(ch[i]);
            int next = map.get(ch[i+1]);

            if(current<next){
                sum-=current;
            }
            else{
                sum+=current;
            }


        }
        sum+=map.get(ch[ch.length-1]);
        return sum;
        
    }
}