class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int ROWS = board.size(), COLS = board[0].size();
        this->ROWS = ROWS;
        this->COLS = COLS;
        
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if ((r == 0 || c == 0 || r == ROWS - 1|| c == COLS - 1)
                    && board[r][c] == 'O'){
                    dfs(board, r, c);
                }
            }
        }

        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (board[r][c] == 'O') board[r][c] = 'X';
            }
        }

        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (board[r][c] == 'T') board[r][c] = 'O';
            }
        }
    }
private:
    int ROWS, COLS;
    void dfs(vector<vector<char>>& board, int r, int c) {
        if (r < 0 || r >= ROWS || 
            c < 0 || c >= COLS || 
            board[r][c] != 'O') return;

        board[r][c] = 'T';
        dfs(board, r + 1, c);
        dfs(board, r - 1, c);
        dfs(board, r, c + 1);
        dfs(board, r, c - 1);
    }
};
