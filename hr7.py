def count_substring(string, sub_string):
    c,i=0,0
    while i < len(string):
            x=string.find(sub_string,i)
            if x==-1:
                break
            else:
                i=x+1
                c+=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)