class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = m + n - 2
        arrangements = math.factorial(moves)
        m_reps = math.factorial(m-1)
        n_reps = math.factorial(n-1)
        return int(arrangements / (m_reps * n_reps))