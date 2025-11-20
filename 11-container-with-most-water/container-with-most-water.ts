function maxArea(height: number[]): number {

    let l:number=0;
    let r:number=height.length-1;

    let maxArea:number=0;

    while(l<r){

        maxArea= Math.max(maxArea,Math.min(height[l],height[r])*(r-l));

        if(height[l]<height[r]){
            l++;
        }
        else{
            r--;
        }
    }

    return maxArea;
    
};