if __name__ == "__main__":
    n = int(input())
    setA = set()
    for i in range(int(n)):
        countryName = input()
        setA.add(countryName)
    print(len(setA))


