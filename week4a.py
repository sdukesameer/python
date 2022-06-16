#Question-1
def frequency(l):
    (minfreqlist,maxfreqlist,newlist)=([],[],[])
    (minfreq,maxfreq,freq)=(len(l),0,0)
    for i in l:
        if i not in newlist:
            newlist.append(i)
    newlist.sort()
    for i in newlist:
        freq=0
        for j in l:
            if j == i:
                freq=freq+1
        if freq==maxfreq:
            maxfreqlist.append(i)
        if freq>maxfreq:
            maxfreqlist=[]
            maxfreq=freq
            maxfreqlist.append(i)
        if freq==minfreq:
            minfreqlist.append(i)
        if freq<minfreq:
            minfreqlist=[]
            minfreq=freq
            minfreqlist.append(i)
    return (minfreqlist,maxfreqlist)
#Question-2
def onehop(l):
    list=[]
    for x in l:
        for y in l:
            if x[1]==y[0]:
                if not(x[0] == y[1]):
                    if (x[0],y[1]) not in list:
                        list.append((x[0],y[1]))
    list.sort()
    return list