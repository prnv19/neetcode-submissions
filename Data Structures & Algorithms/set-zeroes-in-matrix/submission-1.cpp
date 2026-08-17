class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        set<int> zero_rows, zero_cols;
        int ROWS = matrix.size(), COLS = matrix[0].size();

        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (matrix[r][c] == 0){
                    zero_rows.insert(r);
                    zero_cols.insert(c);
                }
            }
        }
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (zero_rows.count(r) || 
                zero_cols.count(c)) matrix[r][c] = 0;
            }
        }
        
    }
};
