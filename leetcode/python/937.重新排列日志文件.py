#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#
from typing import List
import re

# @lc code=start


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            label, content = log.split(' ', 1)
            c = content.split(' ', 1)[0]
            if c.isalpha():  # 字母日志
                return (0, content, label)
            else:
                return (1,)
        return sorted(logs, key=lambda log: get_key(log))

    def helper1(self, logs):
        N = len(logs)
        pos_num_log = -1
        # 调整数字日志位置.
        for i in range(N-1, -1, -1):
            if self.isNumLog(logs[i]):
                j = i
                while j+1 < N and not self.isNumLog(logs[j+1]):
                    logs[j], logs[j+1] = logs[j+1], logs[j]
                    j += 1
                pos_num_log = j
        # 排序字符串日志
        for i in range(0, pos_num_log):
            for j in range(0, pos_num_log-i-1):
                if Solution.strLogCmp(logs[j], logs[j+1]) > 0:
                    logs[j], logs[j+1] = logs[j+1], logs[j]
        return logs

    def isNumLog(self, log: str):
        """
        判断log是否为数字日志.
        """
        _, first = log.split(' ')[:2]
        if re.match(r'\d+', first):
            return True
        else:
            return False

    @staticmethod
    def strLogCmp(a, b):
        l1, c1 = a.split(' ', 1)
        l2, c2 = b.split(' ', 1)
        if c1 != c2:
            if c1 < c2:
                return -1
            else:
                return 1
        else:
            if l1 == l2:
                return 0
            elif l1 < l2:
                return -1
            else:
                return 1

# @lc code=end
