def diagonalDifference(arr):
    diag1 = sum(arr[x][x] for x in range(len(arr)))
    diag2 = sum(arr[x][n-1-x] for x in range(len(arr)))
    return(abs(diag1-diag2))

    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

