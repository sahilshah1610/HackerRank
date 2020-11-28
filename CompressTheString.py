from itertools import groupby
def compressString(s):
    print(*[(len(list(g)), int(k)) for k, g in groupby(s)])
if __name__ == "__main__":
    s = str(input())
    compressString(s)