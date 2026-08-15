class Solution {
public:
    int trap(vector<int>& height) {
        int sz = height.size();
        if (sz == 0) return 0;
        vector<int> maxl(sz), maxr(sz);
        int t = 0;

        for (int i = 0; i < sz; i++) {
            t = max(t, height[i]);
            maxl[i] = t;
        }

        t = 0;
        for (int i = sz - 1; i >= 0; i--) {
            t = max(t, height[i]);
            maxr[i] = t;
        }

        int res = 0;
        for (int i = 0; i < sz; i++) {
            res += min(maxl[i], maxr[i]) - height[i];
        }

        return res;
    }
};
