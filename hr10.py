import textwrap

def wrap(string, max_width):
    res="";w="";c=0
    for l in string:
        w+=l
        c+=1
        if c==max_width:
            res+=w+"\n"
            c=0;w=''
    if c!=0:
        res+=w+"\n"
        c=0;w=''
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)