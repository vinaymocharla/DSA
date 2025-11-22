function groupAnagrams(strs: string[]): string[][] {

    const map1:Map<string,string[] > = new Map();

    for(const str of strs){


        const sortedWord = str.split('').sort().join();

        if(!map1.has(sortedWord)){

            map1.set(sortedWord,[]);
        }
        map1.get(sortedWord)!.push(str)
    }
    

    return Array.from(map1.values())
};