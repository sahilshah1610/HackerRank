if __name__ == '__main__':
    inputArray = list()
    setScores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        inputArray.append([name, score])
        setScores.add(score)
    secondLowest = sorted(setScores)[1]
    secondLowestNames = list()
    for name, score in inputArray:
        if score == secondLowest:
            secondLowestNames.append(name)
    for name in secondLowestNames:
        print(name, end='\n')
