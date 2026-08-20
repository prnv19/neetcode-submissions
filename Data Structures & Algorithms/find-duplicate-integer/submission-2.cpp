class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = 0, slow = 0;
        while (true){
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (fast == slow) break;
        }
        int sslow = 0;
        while (true){
            slow = nums[slow];
            sslow = nums[sslow];
            if (sslow == slow) break;
        }
        return slow;
    }
};
