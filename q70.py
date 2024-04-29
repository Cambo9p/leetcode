def climbStairs(n, mem=None):
    """
    :type n: int
    :rtype: int
    """
    if not mem:
        mem = [-1] * (n + 1)

    if n < 0:
        return 0

    if n == 0:
        return 1

    if mem[n] != -1:
        return mem[n]

    mem[n] = climbStairs(n -1, mem) + climbStairs(n - 2, mem)

    return mem[n]


print(climbStairs(3))
