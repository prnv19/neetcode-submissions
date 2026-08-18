class TimeMap {
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        hashset[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        int m, l = 0, r = hashset[key].size() - 1;
        string result = "";
        while (l <= r){;
            m = (l + r) / 2;
            if (hashset[key][m].first <= timestamp){
                result = hashset[key][m].second;
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }
        return result;
    }
private:
    unordered_map<string, vector<pair<int, string>>> hashset;
};
