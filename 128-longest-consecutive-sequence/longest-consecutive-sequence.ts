function longestConsecutive(nums: number[]): number {

    const set = new Set<number>();

    for(let i of nums){

        set.add(i)
    }
    let longest =0;

    for(let i of set){

        if(!set.has(i-1)){

            let length=1

            while(set.has(i+length)){

                length++;
            }

            longest = Math.max(longest,length)
        }
    }
    
    return longest
};