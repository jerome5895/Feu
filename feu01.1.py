mod = 1000000007

def ValOfTheExpression(n):
    global mod

    factorial = [0 for i in range(n + 1)]
    
    factorial[0] = 1
    factorial[1] = 1

    for i in range(2, n + 1, 1):
        factorial[i] = ((factorial[i - 1] % mod) * (i % mod)) % mod

    dp = [0 for i in range(n + 1)]
    dp[1] = 1

    for i in range(2, n + 1, 1):
        dp[i] = ((dp[i - 1] % mod) * (factorial[i] % mod)) % mod

    return dp[n]

if __name__ == '__main__':
    n = 4
    print(ValOfTheExpression(n))
