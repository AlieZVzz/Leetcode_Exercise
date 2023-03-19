def cut(length):
    dp = [0]*(length+1)
    for i in range(2,length+1):
        for j in range(0,i):
            dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
    return dp[length]

print(cut(8))