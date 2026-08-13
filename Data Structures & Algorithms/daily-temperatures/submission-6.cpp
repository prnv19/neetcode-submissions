class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> temp, t_idx;
        vector<int> res(temperatures.size(), 0);
        for(int i = 0; i < temperatures.size(); i++){
            while (!temp.empty() && temp.back() < temperatures[i]){
                res[t_idx.back()] = i - t_idx.back();
                temp.pop_back();
                t_idx.pop_back();
            }
            temp.push_back(temperatures[i]);
            t_idx.push_back(i);
        }
        return res;
    }
};
