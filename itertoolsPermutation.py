from itertools import permutations
def toolsPermutations(s, k):
    output = list(permutations(sorted(s),int(k)))
    for i in output:
        print(''.join(i))

if __name__ == "__main__":
    s, k = (map(str,input().split()))

    toolsPermutations(s, k)