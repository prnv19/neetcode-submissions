class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> t_idx;
        vector<int> res(temperatures.size(), 0);
        for(int i = 0; i < temperatures.size(); i++){
            while (!t_idx.empty() && temperatures[t_idx.back()] < temperatures[i]){
                res[t_idx.back()] = i - t_idx.back();
                t_idx.pop_back();
            }
            t_idx.push_back(i);
        }
        return res;
    }
};
