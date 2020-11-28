def calHappiness(arr, A, B):
    happiness = 0
    for num in arr:
        if num in A:
            happiness +=1
        if num in B:
            happiness -=1
    print(happiness)

if __name__ == "__main__":
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))
    calHappiness(arr, setA, setB)