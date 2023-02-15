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

#print(FrequencyTable('ACGTTTCACGTTTTACGG',3))
print(FrequencyTable('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA',3))

def Maxmap(freqdict):
    return max(freqdict.values())

def BetterFrequentwords(Texto,k):
    freqpat = []
    freqmap = FrequencyTable(Texto,k)
    maxi = Maxmap(freqmap)
    for x in freqmap:
        if freqmap[x] == maxi:
            freqpat.append(x)
    return freqpat

#print(BetterFrequentwords('ACGTTGCATGTCGCATGATGCATGAGAGCT',4))

