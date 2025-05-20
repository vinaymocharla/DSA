class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> map = new HashMap();


        for(String str: strs){

            char[] word = str.toCharArray();
            Arrays.sort(word);

            String ch =Arrays.toString(word);

            

            if(!map.containsKey(ch)){

                map.put(ch,new ArrayList(){});

               
            }
             map.get(ch).add(str);





        }

        return new ArrayList(map.values());
        
    }
}