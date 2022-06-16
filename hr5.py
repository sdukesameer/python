def swap_case(s):
    l=""
    for w in s:
        if ord(w)>64 and ord(w)<91:
            l+=w.lower()
        elif ord(w)>96 and ord(w)<123:
            l+=w.upper()
        else:
            l+=w
    return l

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)