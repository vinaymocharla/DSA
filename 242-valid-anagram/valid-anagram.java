class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character,Integer> map = new HashMap();


        for(char i : s.toCharArray()){

            map.put(i,map.getOrDefault(i,0)+1);
        }

        for(char ch:t.toCharArray()){

            if (map.containsKey(ch)){

               
                

                map.put(ch,map.get(ch)-1);

                 if(map.get(ch)==0){
                    map.remove(ch);
                }
                

            }
            else{

                return false;
            }


        }

        System.out.print(map.values());

        return map.size()==0;
        
    }
}