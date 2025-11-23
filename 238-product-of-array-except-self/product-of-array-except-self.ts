function productExceptSelf(nums: number[]): number[] {

    let n:number = nums.length


    const leftProduct:number[] = new Array(n);
    const rightProduct:number[] = new Array(n);

    leftProduct[0]=1;
    for(let i=1;i<n;i++){

        leftProduct[i] = leftProduct[i-1]*nums[i-1];
    }

    rightProduct[n-1]=1;
    for(let i=n-2;i>=0;i--){

        rightProduct[i] = rightProduct[i+1]*nums[i+1];
    }

    const result:number[] = new Array(n)

    for(let i=0;i<n;i++){

        result[i] = leftProduct[i]*rightProduct[i];
    }

    return result;




    
};