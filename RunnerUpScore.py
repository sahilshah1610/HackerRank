def runnerUp(arr):
    setItems = sorted(list(set(arr)))

    print(setItems[-2])


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxItem = max(arr)
    while max(arr) == maxItem:
        arr.remove(max(arr))

    print(max(arr))
    #arr = [2,3]
    #runnerUp(arr)

