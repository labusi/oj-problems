#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
class MedianFinder:
    """
    暴力求解, 保存全部曾经插入的数据, 并保证有序.

    优化思路:
        即使是使用暴力求解, 也存在优化空间, 比如确定插入位置的时候使用二分查找的方式.

    题解:
        使用一个最大堆和一个最小堆, 并且使两个堆的元素个数最多相差1.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.n = 0

    def addNum(self, num: int) -> None:
        if self.n == 0:
            self.data.append(num)
        else:  # 插入到合适的位置
            if num > self.data[-1]:
                self.data.append(num)
            else:
                idx = self.__binSearch(num)
                self.data.insert(idx, num)
        self.n += 1

    def __binSearch(self, num):
        """
        使用二分查找确定新数据应该插入的位置.
        """
        a, b = 0, self.n-1
        while b > a:
            mid = (a+b)//2
            if self.data[mid] < num:
                a = mid + 1
            elif self.data[mid] > num:
                # 不能越界
                b = max([mid-1, 0])
            else:
                b = mid
                break
        if self.data[b] < num:
            b += 1
        return b

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return self.data[(self.n-1)//2]
        else:
            a = self.data[self.n//2]
            b = self.data[self.n//2-1]
            return (a+b)/2


# if __name__ == "__main__":
#     mf = MedianFinder()
#     nums = [-1, -2, -3, -4, -5]
#     for num in nums:
#         mf.addNum(num)
#         print(mf.findMedian())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
