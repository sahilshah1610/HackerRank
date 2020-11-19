def sample(string):
    words = string.split()
    newStringList = list(reversed(words))
    #
    newString = (' '.join(newStringList))
    print(newString.swapcase())


    newStringList = list()
    for x in string:
        if x.islower():
             newStringList.append(x.upper())
        else:
             newStringList.append(x.lower())

    print(newStringList)
    # reversedOutput = newString[::-1]
    # print(reversedOutput)





if __name__ == "__main__":
    result = sample("rUns dOg")