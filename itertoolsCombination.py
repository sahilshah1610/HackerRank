from itertools import combinations
def toolsCombinations(s, k):
    for x in range(1,int(k)+1):
        output = list(combinations(sorted(s),int(x)))
        for i in output:
             print(''.join(i))

if __name__ == "__main__":
    s, k = (map(str,input().split()))

    toolsCombinations(s, k)