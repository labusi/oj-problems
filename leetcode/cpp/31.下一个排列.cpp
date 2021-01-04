#include <algorithm>
#include <iostream>

using std::cout;

struct MyPair {
    int i;
    int j;
    int num;
    MyPair(int ii=0, int jj=0, int number=-1) : i(ii), j(jj), num(number) {}

    bool operator<(const MyPair &two) {
        return i < two.i || (i == two.i && num > two.num);
    }

};

// 通过一次交换和一次排序得到下一个排列
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int index = -1;
        int size = nums.size();
        int number = nums[0] < nums[size-1] ? nums[size-1] : -1;
        struct MyPair pair(0, size-1, number);

        for(int i = size - 1; i > 0; --i) {
            for(int j = i - 1; j >= 0; --j) {
                if(nums[i] > nums[j]) {
                    struct MyPair tmp_pair(j, i, nums[i]);
                    if(pair.num == -1 || pair < tmp_pair) {
                        pair = tmp_pair;
                    }
                }
            }
        }
        // cout << pair.i << "\t" << pair.j << "\t" << pair.num << "\n";
        if(pair.num != -1){
            index = pair.i;
            swap(nums, pair.i, pair.j);
        }

        if(index != -1) {
            std::vector<int>::iterator it = nums.begin() + index + 1;
            std::sort(it, nums.end());
        }
        else {
            for(int i = 0; i < size / 2; ++i) {
                swap(nums, i, size - i - 1);
            }
        }

    }
private:
    void swap(vector<int>& nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
};
