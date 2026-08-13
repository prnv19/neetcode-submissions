class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;
        this->grid = grid;
        R = grid.size();
        C = grid[0].size();
        visited.assign(R, vector<bool>(C, false));

        for (int r = 0; r < R; r++){
            for (int c = 0; c < C; c++){
                if (grid[r][c] == 1 && !visited[r][c]){
                    max_area = max(max_area, dfs(r, c));
                }
            }
        }
        return max_area;

    }
private:
    vector<vector<bool>> visited;
    vector<vector<int>> grid;
    int R, C;

    bool valid(int r, int c){
        if (r < 0 || r >= R || c < 0 || c >= C) return false;
        if (grid[r][c] == 0) return false;
        if (visited[r][c]) return false;
        return true;
    }

    int dfs(int r, int c){
        if (!valid(r, c)) return 0;
        visited[r][c] = 1;

        return (1
            + dfs(r + 1, c)
            + dfs(r - 1, c)
            + dfs(r, c + 1)
            + dfs(r, c - 1));
    }
};
