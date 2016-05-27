stri = 'অঅঁকোল'
strlen = len(stri)
dp = []
for i in range(strlen+1):
    dp.append(0)
dp[0] = 1
print(dp)