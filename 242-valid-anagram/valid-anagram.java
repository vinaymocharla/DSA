class Solution {
    public boolean isAnagram(String s, String t) {

       Map<Character,Integer> map = new HashMap();


        for(char i:s.toCharArray()){

            map.put(i,map.getOrDefault(i,0)+1);


        }

        System.out.println(map);

        for(char j:t.toCharArray()){

            if (map.containsKey(j)){

                if (map.get(j)==1){

                    map.remove(j);


                }
                else{
                    map.put(j,map.get(j)-1);

                }
            


            }
            else{
                return false;
            }
        }
         System.out.println(map);

        return map.size()==0;



        
    }
}