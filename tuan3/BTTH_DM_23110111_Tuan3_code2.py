def longest_common_subsequence(source_string, target_string):
    m = len(source_string)
    n = len(target_string)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1 , m + 1):
        dp[i][0] = 0
    
    for j in range(1 , n + 1):
        dp[0][j] = 0

    for i in range(1 , m + 1):
        for j in range(1 , n + 1):
            if source_string[i - 1] == target_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lcss = []

    i = len(source_string)
    j = len(target_string)

    while(i != 0 and j != 0):
        if source_string[i - 1] == target_string[j - 1]:
            lcss.append(source_string[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcss.reverse()

    return [dp[m][n], lcss]

if __name__ == "__main__":
    print("Enter the source string :")
    source_string = input().strip()
    print("Enter the target string :")
    target_string = input().strip()

    ans ,lcss = longest_common_subsequence(source_string, target_string)

    print("The number of longest common subsequence is :", ans)
    print("Longest common subsequence: ", lcss)