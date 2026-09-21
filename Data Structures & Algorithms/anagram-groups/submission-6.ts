class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const mp: Record<string, string[]> = {};
        for (let s of strs) {
            let count: number[] = Array(26).fill(0);
            for (let i = 0; i < s.length; i++) {
                count[s.charCodeAt(i)-'a'.charCodeAt(0)] += 1;
            }
            let key: string = count.join(',');
            if (!mp[key]) {
                mp[key] = [];
            }
            mp[key].push(s);
        }
        return Object.values(mp); 

    }
}
