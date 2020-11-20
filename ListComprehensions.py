def listComprehensions(x, y, z, n):
    combinations = [[a,b,c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1)]
    resultArray = list()
    for arr in combinations:
        if sum(arr) != n:
            resultArray.append(arr)
    print(resultArray)
    pass


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listComprehensions(x, y, z, n)