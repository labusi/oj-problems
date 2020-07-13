/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        vector<int> ans;
        int m = matrix.size();
        if (m == 0)
        {
            return ans;
        }
        int n = matrix[0].size();
        if (n == 0)
        {
            return ans;
        }
        int count = 0;
        int a = 0, b = 0;
        int c = m - 1, d = n - 1;

        while (count < m * n)
        {
            //top
            for (int i = b; i <= d; i++)
            {
                ans.push_back(matrix[a][i]);
                count += 1;
            }
            //right
            for (int i = a + 1; i <= c; i++)
            {
                ans.push_back(matrix[i][d]);
                count += 1;
            }
            //bottom
            for (int i = d - 1; c > a && i >= b; i--)
            {
                ans.push_back(matrix[c][i]);
                count += 1;
            }
            //left
            for (int i = c - 1; b < d && i > a; i--)
            {
                ans.push_back(matrix[i][b]);
                count += 1;
            }
            a += 1;
            b += 1;
            c -= 1;
            d -= 1;
        }
        return ans;
    }
};
// @lc code=end
