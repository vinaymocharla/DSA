class Solution {
    public List<String> letterCombinations(String digits) {
        Map<Character, String > map = new HashMap();
        List<String>  result = new ArrayList();

        if (digits.length()==0 || digits==null){
            return result;
        }
        

        map.put('2',"abc");
        map.put('3',"def");
        map.put('4',"ghi");
        map.put('5',"jkl");
        map.put('6',"mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        backtrack(0, digits, map,new StringBuilder(), result);
        return result;

        



        
    }

    private void backtrack(int index, String digits, Map<Character, String> map, StringBuilder current, List<String> result ){


        if(index==digits.length()){
            result.add(current.toString());
            return;
        }

        String letters  = map.get(digits.charAt(index));

        for(char ch : letters.toCharArray()){

            current.append(ch);

            backtrack(index+1, digits,map,current,result);

            current.deleteCharAt(current.length()-1);
        }
    }
}