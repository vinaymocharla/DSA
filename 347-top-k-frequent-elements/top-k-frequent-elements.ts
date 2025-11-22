function topKFrequent(nums: number[], k: number): number[] {

    const freqMap: Map<number,number> = new Map();


    for(const num of nums ){

        freqMap.set(num,(freqMap.get(num)??0)+1)
    }
    const bucket: number[][] = Array.from({length:nums.length+1},()=>[]);

    for(const[num,freq] of freqMap.entries()){

        bucket[freq].push(num);
    }

    const res : number[] = [];

    for(let i=bucket.length-1;i>0;i--){

        if(bucket[i].length>0){

            res.push(...bucket[i])
        }
        if(res.length>=k){
            return res;
        }
    }
};