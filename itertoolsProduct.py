import itertools
def product(a, b):
    print(*itertools.product(a,b))
if __name__ == "__main__":
    arrayA = list(map(int, input().split()))
    arrayB = list(map(int, input().split()))
    product(arrayA, arrayB)