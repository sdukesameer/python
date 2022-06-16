def split_and_join(line):
    r = line.split(" ")
    l = "-".join(r)
    return l

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)