class Solution {
public:
    int minDistance(string word1, string word2) {
        int rows = word1.size() + 1, cols = word2.size() + 1;
        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        
        for (int c = 0; c < cols - 1; c++) dp[rows - 1][c] = cols - 1 - c; 
        for (int r = 0; r < rows - 1; r++) dp[r][cols - 1] = rows - 1 - r;

        // for (int i = 0; i < dp.size(); i++) {
        // for (int j = 0; j < dp[i].size(); j++) {
        //     cout << dp[i][j] << " ";
        //     }
        // cout << endl;
        // }
        for (int r = rows - 2; r >= 0; r--){
            for (int c = cols - 2; c >= 0; c--){
                if (word1[r] == word2[c]) dp[r][c] = dp[r + 1][c + 1];
                else dp[r][c] = 1 + min({dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1]});
            }
        }
        return dp[0][0];
    }
};
