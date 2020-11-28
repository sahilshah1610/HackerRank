from itertools import combinations_with_replacement
def toolsCombinationsReplacement(s, k):
    output = list(combinations_with_replacement(sorted(s),int(k)))
    for i in output:
        print(''.join(i))

if __name__ == "__main__":
    s, k = (map(str,input().split()))

    toolsCombinationsReplacement(s, k)