class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        
        R = grid.size();
        C = grid[0].size();
        visited = vector<vector<int>>(R, vector<int>(C, 0));

        this->grid = grid;
        this->visited = visited;

        int res = 0;
        for(int r = 0; r < R; r++){
            for(int c = 0; c < C; c++){
                if (grid[r][c] == '1' && visited[r][c] == 0){
                    res++;
                    dfs(r, c);
                }
            }
        }

        return res;
    }
private:
    vector<vector<int>> visited;
    vector<vector<char>> grid;

    int R, C;
    
    bool valid(int r, int c){
        if (r < 0 || r >= R || c < 0 || c >= C || visited[r][c] == 1 || grid[r][c] == '0') return false;
        return true;
    }

    void dfs(int r, int c){
        if (!valid(r, c)) return;
        visited[r][c] = 1;
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    }

};
