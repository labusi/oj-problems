#include <vector>
using std::vector;

class Solution {
public:
  int searchInsert(vector<int>& nums, int target) {
    int index = 0;
    for(; index < nums.size(); ++index){
      if(nums[index] >= target)
        break;
    }
    return index;
  }
};
