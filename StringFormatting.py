def print_formatted(number):
    # your code goes here

    spacing = len(bin(number).replace('0b', ''))
    print(spacing)
    for i in range(1, number+1):
        decimal = str(i).rjust(spacing,' ')
        octal = str(oct(i).replace('0o', '')).rjust(spacing, ' ')
        hexa = str(hex(i).replace('0x', '').upper()).rjust(spacing, ' ')
        binary = str(bin(i).replace('0b', '')).rjust(spacing, ' ')
        print(decimal,octal, hexa, binary)
if __name__ == "__main__":
    n = int(input())
    print_formatted(n)