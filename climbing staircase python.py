def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Example usage:
n_steps = int(input("Enter the number of steps: "))
distinct_ways = climbStairs(n_steps)
print(f"Distinct ways to climb to the top: {distinct_ways}")
