class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> target_count(26, 0);
        vector<int> count(26, 0);

        for (int i = 0; i < s1.size(); i++){
            target_count[(int)s1[i] - (int)'a'] += 1;
        }
        
        int l = 0;
        for (int r = 0; r < s2.size(); r++){
            count[(int)s2[r] - (int)'a'] += 1;
            if (r - l + 1 > s1.size()){
                count[(int)s2[l] - (int)'a'] -= 1;
                l++;
            }
            if (count == target_count) return true;
        }
        return false;
    }
};
