n=[]
s=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n.append(name)
        s.append(score)
m0=min(s)
m1=101.0;l=[]

for i in range(len(s)):
    if s[i] < m1 and s[i] > m0:
        m1=s[i]

for i in range(len(n)):
    if s[i] == m1:
        l.append(n[i])
l=sorted(l)
for i in range(len(l)):
    print(l[i])