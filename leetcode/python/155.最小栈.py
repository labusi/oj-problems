#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.min_val = 1e64

    def push(self, x: int) -> None:
        self.arr.append(x)
        if x < self.min_val:
            self.min_val = x

    def pop(self) -> None:
        if self.min_val == self.arr[-1]:
            self.min_val = 1e64
            for num in self.arr[:-1]:
                if self.min_val > num:
                    self.min_val = num
        self.arr.pop(-1)

    def top(self) -> int:
        if len(self.arr) == 0:
            return None
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
