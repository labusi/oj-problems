/*
 * @lc app=leetcode.cn id=1000 lang=cpp
 *
 * [1000] 合并石头的最低成本
 */

// @lc code=start
#include <vector>
#include <iostream>
using namespace std;

/**
 * 
 * 并不是每次选最小的.
*/
class Solution
{
public:
    int mergeStones(vector<int> &stones, int K)
    {
        int n = stones.size();
        if ((n - 1) % (K - 1) != 0)
        {
            return -1;
        }
        int ans = 0;
        vector<char> marked(n, 0);
        int x = (n - 1) / (K - 1);
        while (x > 0)
        {
            int sum = 0x7fffffff;
            int start = -1, end = -1;
            for (int i = 0; i <= n - K; i++)
            {
                int e = -1;
                int tmp = getSum(stones, marked, i, e, K);
                if (sum > tmp)
                {
                    sum = tmp;
                    start = i;
                    end = e;
                }
            }
            ans += sum;
            after(stones, marked, start, end, sum);
            x -= 1;
        }
        return ans;
    }

private:
    int getSum(vector<int> &stones, vector<char> &marked, int s, int &e, int k)
    {
        int sum = 0, p = s;
        int n = stones.size();
        while (k > 0)
        {
            if (p >= n)
            {
                break;
            }
            if (marked[p] == 0)
            {
                sum += stones[p];
                k -= 1;
            }
            p++;
        }
        if (k != 0)
        {
            return 0x7fffffff;
        }
        else
        {
            e = p;
            return sum;
        }
    }

    void after(vector<int> &stones, vector<char> &marked, int s, int e, int sum)
    {
        for (int i = s; i < e - 1; i++)
        {
            marked[i] = 1;
        }
        marked[e - 1] = 0;
        stones[e - 1] = sum;
    }
};

// @lc code=end
