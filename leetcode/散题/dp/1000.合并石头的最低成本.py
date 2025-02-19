class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - k) % (k - 1):
            return -1
        N = 31
        f = [[float("inf") for _ in range(N)]for _ in range(N)]
        for i in range(n + 1):
            f[i][i] = 0
        s = [0] * N
        for i in range(1,n + 1):
            s[i] = s[i - 1] + stones[i - 1]

        for i in range(n,0,-1):
            for j in range(i + 1,n + 1):
                for m in range(i,j,k - 1):
                    f[i][j] = min(f[i][j],f[i][m] + f[m + 1][j])
                if (j - i) % (k - 1) == 0:
                    f[i][j] += s[j] - s[i - 1]
        return f[1][n]
        
         