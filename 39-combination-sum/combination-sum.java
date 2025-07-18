class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        List<List<Integer>> result = new ArrayList();

        List<Integer> list = new ArrayList();

        backtrack(0,0,candidates, target, list, result);

        return result;
        
    }


    public void backtrack(int start, int sum, int[] candidates, int target,List<Integer> list,List<List<Integer>> result  ){


        if(sum==target){

            result.add(new ArrayList(list));

            return;
        }

        if (sum> target){

            return;
        }

        for(int i=start; i< candidates.length;i++){

            list.add(candidates[i]);

            if(sum<=target){

                backtrack(i, sum+candidates[i],candidates, target, list,result);

                list.remove(list.size()-1);
            }
        }
    }
}