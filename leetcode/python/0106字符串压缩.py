class Solution:
    def compressString(self, S: str) -> str:
        return self.doublePointer2(S)

    def basicMethod(self, S: str) -> str:
        '''
        基本方法.
        '''
        if S == '':
            return S

        tag = S[0]
        n = 0
        S2 = ''
        for ch in S:
            if ch == tag:
                n += 1
            else:
                S2 += tag + str(n)
                tag = ch
                n = 1
        S2 += tag + str(n)

        if len(S2) >= len(S):
            return S
        else:
            return S2

    def doublePointer(self, S: str) -> str:
        '''
        双指针法, 计算连续字符串.
        '''
        if S == '':
            return S

        i, j = 0, 0
        S2 = ''

        while j < len(S):
            if S[i] == S[j]:
                j += 1
            else:
                S2 += S[i] + str(j-i)
                i = j

        S2 += S[i] + str(j-i)

        if len(S2) >= len(S):
            return S
        else:
            return S2

    def doublePointer2(self, S: str) -> str:
        '''
        另一种写法, 双指针.
        '''
        if S == '':
            return S

        i = 0
        N = len(S)
        S2 = ''

        while i < N:
            j = i
            while j < N and S[i] == S[j]:
                j += 1
            S2 += S[i] + str(j-i)
            i = j

        if len(S2) >= N:
            return S
        else:
            return S2


if __name__ == "__main__":
    s = Solution()
    print(s.compressString('aabbbbCCC'))
