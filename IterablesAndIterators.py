from itertools import combinations
def ablesAndTors(N, arrayN, K):
    combinationsGroped = list(combinations(arrayN,K))
    matches = [i for i in combinationsGroped if 'a' in i]
    print("{:.4f}".format(len(matches)/len(combinationsGroped)))
if __name__ == "__main__":
    N = int(input())
    arrayN = list(map(str, input().split()))
    K = int(input())
    ablesAndTors(N,arrayN, K)