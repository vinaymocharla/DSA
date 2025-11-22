function groupAnagrams(strs: string[]): string[][] {
    
    const map1: Map<string, string[]> = new Map();
    for(const str of strs){

        const sortedString : string= str.split('').sort().join('');

        if(!map1.has(sortedString)){

            map1.set(sortedString,[]);
        }

        map1.get(sortedString).push(str);


    }

    const  result:string[][] =[...map1.values()];

    return result


    
};