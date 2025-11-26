function isPalindrome(s: string): boolean {

    s= s.replace(/[^a-zA-Z0-9]/g,'').toLowerCase()

    let l:number=0;
    let r:number = s.length-1

    while(l<=r){



        if(s[l]!=s[r]){
            return false
    
    
        }

        l++;
        r--;
    }

    return true


    
};