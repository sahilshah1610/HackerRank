def difference(m,n):
    differenceSet = list(set(m).difference(set(n))) + list(set(n).difference(set(m)))
    for x in sorted(differenceSet):
        print(x)

if __name__ == "__main__":
    M = int(input())
    arrM = list(map(int, input().split()))
    N = int(input())
    arrN = list(map(int, input().split()))
    difference(arrM, arrN)