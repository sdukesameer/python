d={}
fh=open(r"c:\Users\SAMEER\CODEINGSPACE\py\2nd.txt")
for line in fh:
    l=[]
    for word in line.split("_"):
        if '(' in word:
            word=word[0:word.index('(')]
        l.append(word.strip())
    d[l[1]]=d.get(l[1],0)+1
d={key: value for key, value in sorted(d.items(), key=lambda item: item[1], reverse=True)}
for k,v in d.items(): 
    print("{}: {}".format(k,v))