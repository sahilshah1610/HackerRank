def swap_case(s):
    output = ""
    listS = list(s)
    for index, ch in enumerate(listS):
        if ch.islower():
            listS[index] = ch.upper()
        elif ch.isupper():
            listS[index] = ch.lower()
            
    return ''.join(listS)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)