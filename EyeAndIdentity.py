import numpy
if __name__ == "__main__":
    x, y = map(int,input().split())
    print(numpy.eye(x, y))
