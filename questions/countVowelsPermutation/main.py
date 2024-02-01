class Solution:
    def countVowelPermutation(self, n: int) -> int:

        cols = [[1,1,1,1,1]]
        a, e, i, o, u = 0,1,2,3,4

        mod = 10**9 + 7

        for j in range(n-1):
            newCol = [0,0,0,0,0]
            newCol[a] = (cols[j][e] + cols[j][i] + cols[j][u]) % mod
            newCol[e] = (cols[j][a] + cols[j][i] ) % mod
            newCol[i] = (cols[j][e] + cols[j][o] ) % mod
            newCol[o] = (cols[j][i]) % mod
            newCol[u] = (cols[j][i] + cols[j][o]) % mod
            cols.append(newCol)
        
        return sum(cols[n-1]) % mod
        