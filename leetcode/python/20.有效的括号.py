#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']': '[', ')': '(', '}': '{'}
        stack = []
        for ss in s:
            if ss not in brackets:
                stack.append(ss)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() != brackets[ss]:
                        return False

        return len(stack) == 0

# @lc code=end

