
def twoStrings(s1, s2):
    splitString1 = list(s1)
    splitString2 = list(s2)
    print(splitString1)
    print(splitString2)
    for x in range(len(splitString1)):
        if splitString1[x] in splitString2:
            return "YES"

    return "NO"

s1 = "hello"
s2 = "world"
print(twoStrings(s1, s2))