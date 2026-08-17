class Solution {
public:
    bool canPartition(vector<int>& nums) {
        if (accumulate(nums.begin(), nums.end(), 0) % 2 == 1) return false;
        unordered_set<int> dp;
        dp.insert(0);
        int target = accumulate(nums.begin(), nums.end(), 0) / 2;

        for (int i = nums.size() - 1; i >= 0; i--){
            unordered_set<int> new_dp;
            for (int val : dp){
                new_dp.insert(val);
                new_dp.insert(val + nums[i]);
            }
            dp = new_dp;
        }

        if (dp.find(target) != dp.end())return true;
        return false;
    }
};
