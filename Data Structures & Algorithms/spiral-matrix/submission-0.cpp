class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int T = 0, B = matrix.size() - 1, L = 0, R = matrix[0].size() - 1;
        vector<int> res;

        while (L <= R && T<= B){
            //L -> R
            for (int i = L; i <= R; i++){
                res.push_back(matrix[T][i]);
            }
            T++;
            //T -> B
            for (int i = T; i <= B; i++){
                res.push_back(matrix[i][R]);
            }
            R--;
            //R -> L
            if (T > B) break;
            for (int i = R; i >= L; i--){
                res.push_back(matrix[B][i]);
            }
            B--;
            //B->T
            if (L > R) break;
            for (int i = B; i >= T; i--){
                res.push_back(matrix[i][L]);
            }
            L++;
        }
        return res;
        
    }
};
