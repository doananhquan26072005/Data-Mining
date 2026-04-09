def dynamic_time_warping(A, B):
    m = len(A)
    n = len(B)

    DTW = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1 , m + 1):
        DTW[1][i] = abs(A[0] - B[i - 1]) + DTW[1][i - 1]
        
    for j in range(1 , n + 1):
        DTW[j][1] = abs(A[j - 1] - B[0]) + DTW[j - 1][1]

    for i in range(2 , m + 1):
        for j in range(2 , n + 1):
            DTW[i][j] = abs(A[i - 1] - B[j - 1]) + min(DTW[i - 1][j], DTW[i][j - 1], DTW[i - 1][j - 1])

    wraping_road = []

    i = len(A)
    j = len(B)

    while(i != 1 and j != 1):
        wraping_road.append(DTW[i][j])
        Min = min(DTW[i - 1][j], DTW[i][j - 1], DTW[i - 1][j - 1])
        if Min == DTW[i - 1][j]:
            i -= 1
        elif Min == DTW[i][j - 1]:
            j -= 1
        else:
            i -= 1
            j -= 1
    
    while(i != 1):
        wraping_road.append(DTW[i][1])
        i -= 1

    while(j != 1):
        wraping_road.append(DTW[1][j])
        j -= 1
    wraping_road.append(DTW[1][1])

    return wraping_road

if __name__ == "__main__":
    A = [1, 7, 4, 8, 2, 9, 6, 5, 2, 0]
    B = [1, 2, 8, 5, 5, 1, 9, 4, 6, 5]

    print("Wraping road is :", dynamic_time_warping(A, B))