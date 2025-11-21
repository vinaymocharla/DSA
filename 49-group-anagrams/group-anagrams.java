class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        List<List<String>> list = new ArrayList();

        Map<String, List<String>> map = new HashMap();

        for(String word : strs){

            char[] ch = word.toCharArray();
            Arrays.sort(ch);
            String sortedword = Arrays.toString(ch);

            if(!map.containsKey(sortedword)){
                map.put(sortedword,new ArrayList());
            }
            map.get(sortedword).add(word);
            
        }

        return new ArrayList(map.values());
        
    }
}