import numpy as np

def Text(i, k, Pat):
    return (Pat[i:(i+k)])

def PatternCount(Texto, Pat):
    count = 0
    for i in range(len(Texto)-len(Pat)+1):
        if Text(i, len(Pat), Texto)==Pat :
            count +=1
    return count

def Frequentwords(Texto, k):
    Freqpat = []
    Count = []
    for i in range(len(Texto)-k+1):
        pat = Text(i,k,Texto)
        Count.append(PatternCount(Texto, pat))
    maxCount = np.max(Count)
    for i in range(len(Texto)-k+1):
        if Count[i] == maxCount:
            Freqpat.append(Text(i,k,Texto))
    Freqpat = np.unique(Freqpat)
    return Freqpat

#print(Frequentwords('ACTGACTCCCACCCC', 3))

#print(Frequentwords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))

print(Frequentwords('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA',4))