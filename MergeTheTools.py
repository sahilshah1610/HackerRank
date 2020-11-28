def merge_the_tools(string, k):
    lenString = len(string)
    for x in range(0,lenString, k):
        subString = string[x:x+k]
        print("".join(set(subString)))


    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)