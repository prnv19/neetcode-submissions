class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> counts;
        int maxf = 0, l = 0, r = 0;

        while (r < s.size()){
            counts[s[r]] += 1;
            maxf = max(maxf, counts[s[r]]);

            while (r - l + 1 - maxf > k){
                counts[s[l]] -= 1;
                l ++;
            }
            r++;
        }
        return r - l;
    }
};
