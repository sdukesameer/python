if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        com=input();
        if com.startswith("insert"):
            l.insert(int(com[com.find(" ")+1: com.find(" ",com.find(" ")+1)]),int(com[com.find(" ",com.find(" ")+1):]))
        elif com=="print":
            print(l)
        elif com.startswith("remove"):
            l.remove(int(com[com.find(" "):]))
        elif com.startswith("append"):
            l.append(int(com[com.find(" "):]))
        elif com=="sort":
            l.sort()
        elif com=="pop":
            l.pop()
        elif com=="reverse":
            l.reverse()
        else:
            print("")