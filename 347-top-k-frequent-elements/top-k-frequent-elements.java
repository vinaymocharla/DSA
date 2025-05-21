class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer,Integer> map = new HashMap<>();

        ArrayList<Integer>[] freq = new ArrayList[nums.length+1];

        for(int i:nums){


            map.put(i,map.getOrDefault(i,0)+1);
        }


        for(int i:map.keySet()){

            int value = map.get(i);


            if(freq[value]==null){

                freq[value] = new ArrayList();
            }

            freq[value].add(i);
        }


        int[] res = new int[k];
        int a=0;


        for(int i=freq.length-1;i>=0;i--){


            if(freq[i]!=null){

                for(int j:freq[i]){

                    if(a>=k){
                        break;
                    }
                    res[a++]=j;
                }





            }
        }

        return res;


       




        
    }
}