class Solution {
    public List<List<Integer>> permute(int[] nums) {

        List<List<Integer>> result = new ArrayList();
        List<Integer> list = new ArrayList();



        backtrack(nums, list, result);

        return result;







        
    }

    public void backtrack(int[] nums, List<Integer> list,List<List<Integer>> result){

        if(list.size()==nums.length){
            
            result.add(new ArrayList(list));
            return;
        }

        for(int i=0;i<nums.length;i++){

            if(list.contains(nums[i])){
                continue;

            }
            list.add(nums[i]);
            
           

            backtrack(nums,list,result);

            
            list.remove(list.size()-1);

            

            






        }
    }
}