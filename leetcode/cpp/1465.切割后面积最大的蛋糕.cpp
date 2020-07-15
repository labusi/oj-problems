/*
 * @lc app=leetcode.cn id=1465 lang=cpp
 *
 * [1465] 切割后面积最大的蛋糕
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    /**
     * 
     * 最大的蛋糕由最大的长宽决定. 给定的输入可能是乱序的.
    */
    int maxArea(int h, int w, vector<int> &horizontalCuts, vector<int> &verticalCuts)
    {
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());
        unsigned maxH = max(horizontalCuts[0], h - horizontalCuts[horizontalCuts.size() - 1]);
        unsigned maxW = max(verticalCuts[0], w - verticalCuts[verticalCuts.size() - 1]);
        for (int i = 1; i < horizontalCuts.size(); i++)
        {
            maxH = max(horizontalCuts[i] - horizontalCuts[i - 1], maxH);
        }

        for (int j = 1; j < verticalCuts.size(); j++)
        {
            maxW = max(verticalCuts[j] - verticalCuts[j - 1], maxW);
        }
        //如果int相乘的话可能会溢出
        unsigned ans = (((long)maxH) * ((long)maxW)) % 1000000007;
        return ans;
    }

    int max(int a, int b)
    {
        return a >= b ? a : b;
    }
};

// @lc code=end
