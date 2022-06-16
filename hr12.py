def print_formatted(n):
    l=len(bin(n))-2
    for i in range(1,n+1):
        o=oct(i)[2:].upper()
        h=hex(i)[2:].upper()
        b=bin(i)[2:]
        print(str(i).rjust(l," "),o.rjust(l," "),h.rjust(l," "),b.rjust(l," "),sep=" ")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)