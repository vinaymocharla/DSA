class Solution {
    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> result = new ArrayList();

        List<Integer> list = new ArrayList();

        backtrack(0,nums,list,result);

        return result;


        
    }


    public void backtrack(int start, int[] nums,List<Integer> list,List<List<Integer>> result  ){

        result.add(new ArrayList(list));

        for(int i=start;i<nums.length;i++){

            list.add(nums[i]);

            backtrack(i+1, nums,list,result);

            list.remove(list.size()-1);
        }
    }
}