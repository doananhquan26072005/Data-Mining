def find_minimum_edit_distance(source_string, target_string):
    m = len(source_string)
    n = len(target_string)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1 , m + 1):
        dp[i][0] = i
    
    for j in range(1 , n + 1):
        dp[0][j] = j

    operations_performed = []

    for i in range(1 , m + 1):
        for j in range(1 , n + 1):
            if source_string[i - 1] == target_string[j - 1]:
                a = 0
            else:
                a = 2
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + a)
    
    i = len(source_string)
    j = len(target_string)

    while(i != 0 and j != 0):
        if source_string[i - 1] == target_string[j - 1]:
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j - 1] + 2:
                operations_performed.append(('REPLACEMENT', source_string[i - 1], target_string[j - 1]))
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + 1: 
                operations_performed.append(('DELETE', source_string[i - 1]))
                i -= 1
            else:
                operations_performed.append(('INSERT', target_string[j - 1]))
                j -= 1
        
    while (i != 0):
        operations_performed.append(('DELETE', source_string[i - 1]))
        i -= 1

    while (j != 0):
        operations_performed.append(('INSERT', target_string[j - 1]))
        j -= 1

    operations_performed.reverse()
    return [dp[m][n], operations_performed]

if __name__ == "__main__":
    print("Enter the source string :")
    source_string = input().strip()
    print("Enter the target string :")
    target_string = input().strip()

    distance, operations_performed = find_minimum_edit_distance(source_string, target_string)

    insertions, deletions, replacements = 0, 0, 0
    for i in operations_performed:
        if i[0] == 'INSERT':
            insertions += 1
        elif i[0] == 'DELETE':
            deletions += 1
        else:
            replacements += 1

    print("Minimum edit distance : {}".format(distance))
    print("Number of insertions : {}".format(insertions))
    print("Number of deletions : {}".format(deletions))
    print("Number of replacements : {}".format(replacements))
    print("Total number of operations : {}".format(insertions + deletions + replacements))

    print("Actual Operations :")
    for i in range(len(operations_performed)):
        
        if operations_performed[i][0] == 'INSERT':
            print("{}) {} : {}".format(i + 1, operations_performed[i][0], operations_performed[i][1]))
            
        elif operations_performed[i][0] == 'DELETE':
            print("{}) {} : {}".format(i + 1, operations_performed[i][0], operations_performed[i][1]))

        else: 
            print("{}) {} : {} by {}".format(i + 1, operations_performed[i][0], operations_performed[i][1], operations_performed[i][2]))
