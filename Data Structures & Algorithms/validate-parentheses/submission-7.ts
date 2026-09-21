class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        let stack = [];
        let starts = new Set(['(', '{', '[']);
        let ends  = new Map<string, string>([
        ["}", "{"],
        ["]", "["],
        [")", "("]
        ]);

        for (const letter of s){
            if (starts.has(letter)) {
                stack.push(letter)
            }
            else if (!starts.has(letter) && !ends.has(letter)) {
                return false;
            }
            else if (ends.has(letter)) {
                if (stack.at(-1) !== ends.get(letter)) {
                    return false;
                }
                else stack.splice(stack.length-1, 1)
            }
        }
        return stack.length === 0;
    }
}
