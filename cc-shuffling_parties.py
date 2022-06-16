import random
t=int(input())
for i in range(t):
    n=int(input())
    A=map(int,input().split())
    random.shuffle(A)
    print(A)