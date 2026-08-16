class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int r = *max_element(piles.begin() , piles.end());
        int l = 1;
        int best = r;
        int hours, m;
        while (l <= r){
            m = (l + r) / 2;
            hours = 0;
            for (int p = 0; p < piles.size(); p++){
                hours += ceil((double)piles[p] / m);
            }
            if (hours <= h){
                best = m;
                r = m - 1;
            }
            else l = m + 1;
        }
        return best;
    }
};
