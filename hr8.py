if __name__ == '__main__':
    s = input()
    #In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
    c=0
    for w in s:
        if (ord(w)>64 and ord(w)<91) or (ord(w)>96 and ord(w)<123) or (ord(w)>47 and ord(w)<58):
            c=1
            break
    if c==1:
        print("True")
    else:
        print("False")
    #In the second line, print True if S has any alphabetical characters. Otherwise, print False.
    c=0
    for w in s:
        if (ord(w)>64 and ord(w)<91) or (ord(w)>96 and ord(w)<123):
            c=1
            break
    if c==1:
        print("True")
    else:
        print("False")
    #In the third line, print True if S has any digits. Otherwise, print False.
    c=0
    for w in s:
        if ord(w)>47 and ord(w)<58:
            c=1
            break
    if c==1:
        print("True")
    else:
        print("False")
    #In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
    c=0
    for w in s:
        if ord(w)>96 and ord(w)<123:
            c=1
            break
    if c==1:
        print("True")
    else:
        print("False")
    #In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
    c=0
    for w in s:
        if ord(w)>64 and ord(w)<91:
            c=1
            break
    if c==1:
        print("True")
    else:
        print("False")