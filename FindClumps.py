import numpy as np

def Text(i, k, Pat):
    return (Pat[i:(i+k)])

def FrequencyTable(Texto,k):
    freqmap = {}
    for i in range(len(Texto)-k+1):
        pat = Text(i, k, Texto)
        if pat not in freqmap.keys():
            freqmap[pat] = 1
        else:
            freqmap[pat] = freqmap[pat] + 1
    return freqmap

def FindClumps(Texto, k, L, t):
    pat = []
    for i in range(len(Texto)-L+1):
        window = Text(i,L,Texto)
        freqmap = FrequencyTable(window, k)
        for x in freqmap.keys():
            if freqmap[x] >= t:
                pat.append(x)
    pat = np.unique(pat)
    return pat

#print(FindClumps('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA',5,50,4))


