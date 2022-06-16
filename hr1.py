if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
l=list(arr)
m=max(l)
l.sort()
for i in range(n-1,-1,-1):
    if l[i]!=m:
        print(l[i])
        break