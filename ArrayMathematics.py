import numpy as np
if __name__ == "__main__":
    n,m = map(int, input().split())
    arrA = np.zeros((n,m),int)
    arrB = np.zeros((n,m),int)
    for i in range(n):
        arrA[i] = np.array(input().split(), int)
    for i in range(n):
        arrB[i] = np.array(input().split(), int)
    print(arrA + arrB)
    print(arrA - arrB)
    print(arrA * arrB)
    print(arrA // arrB)
    print(arrA % arrB)
    print(arrA ** arrB)
