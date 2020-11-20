def validation(s):
    for cmds in ('isalnum()', 'isalpha()', 'isdigit()', 'islower', 'isupper'):
        print(any(eval("c."+cmds) for c in s))

if __name__ == '__main__':
    s = input()
    validation(s)