class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isAlphaNum(char) {
        return (
            (char >= 'a' && char <= 'z') || 
            (char >= 'A' && char <= 'Z') || 
            (char >= '0' && char <= '9')
        );
    }
    isPalindrome(s: string): boolean {
        let start = 0;
        let end = s.length-1;
        while (start < end) {
            while (start < end && !this.isAlphaNum(s[start])) {
                start++;
            }
            while (start < end && !this.isAlphaNum(s[end])) {
                end--;
            }
            if (s[start].toLowerCase() !== s[end].toLowerCase()) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
