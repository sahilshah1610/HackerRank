if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        cmds = input().split()
        if cmds[0] == 'insert':
            arr.insert(int(cmds[1]), int(cmds[2]))
        elif cmds[0] == 'print':
            print(arr)
        elif cmds[0] == 'remove':
            for i in arr:
                if i == int(cmds[1]):
                    arr.remove(i)
                    break
        elif cmds[0] == 'append':
            arr.append(int(cmds[1]))
        elif cmds[0] == 'sort':
            arr.sort()
        elif cmds[0] == 'pop':
            arr.pop()
        elif cmds[0] == 'reverse':
            arr.reverse()




