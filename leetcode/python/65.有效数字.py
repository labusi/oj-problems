#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start


class Solution:

    table = [
        [1, 2, 3, -1, -1],
        [-1, 2, 3, -1, -1],
        [-1, 4, 5, 6, -1],
        [-1, 7, -1, -1, -1],
        [-1, 4, 8, 6, -1],
        [-1, 7, -1, 6, -1],
        [9, 10, -1, -1, -1],
        [-1, 7, -1, 6, -1],
        [-1, 8, -1, 6, -1],
        [-1, 10, -1, -1, -1],
        [-1, 10, -1, -1, -1]
    ]

    finals = [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1]

    def isNumber(self, s: str) -> bool:
        return Solution.dfa(s)

    @staticmethod
    def dfa(s: str) -> bool:
        s = s.strip()
        q = 0  # DFA的初始状态
        for ch in s:
            q = Solution.move(q, ch)
            # 跟踪状态转换
            # print("state: %d" % (q))
            if q == -1:
                return False
        return Solution.finals[q] == 1

    @staticmethod
    def move(q: int, ch):
        if ch in '+-':
            idx = 0
        elif ch in '0123456789':
            idx = 1
        elif ch in '.':
            idx = 2
        elif ch in 'e':
            idx = 3
        else:
            idx = 4
        return Solution.table[q][idx]
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.isNumber('.4e3'))
