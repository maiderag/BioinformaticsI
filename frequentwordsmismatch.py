def FrequencyTable(Texto,k):
    freqmap = {}
    for i in range(len(Texto)-k+1):
        pat = Text(i, k, Texto)
        if pat not in freqmap.keys():
            freqmap[pat] = 1
        else:
            freqmap[pat] = freqmap[pat] + 1
    return freqmap

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

def Hamming(p,q):
    count =0
    for i in range(len(p)):
        if p[i]!=q[i]:
            count +=1
    return count


def Neighbors(pat,d):
    nucleotide = ['A','C','G','T']
    if d==0:
        return pat
    if len(pat) ==1:
        return nucleotide
    Neighboorhood = set()
    Suffixneighbors = Neighbors(pat[1:len(pat)],d)
    for i in Suffixneighbors:
        if Hamming(i, pat[1:len(pat)])<d:
            for j in nucleotide:
                Neighboorhood.add(j+i)
        else:
            Neighboorhood.add(pat[0]+i)
    return Neighboorhood
    

def Frequentwordsmismatch(Texto, k,d):
    freqMap = {}
    patterns = []
    for i in range(len(Texto)-k+1):
        pat = Texto[i:(i+k)]
        neighborhood = list(Neighbors(pat,d))
        for j in range(len(neighborhood)-1):
            neighbor = neighborhood[j]
            if neighbor not in freqMap.keys():
                freqMap[neighbor] =1
            else:
                freqMap[neighbor] += 1
    m =Maxmap(freqMap)
    print(len(freqMap))
    for i in freqMap.keys():
        if freqMap[i] == m:
            patterns.append(i)
    return patterns

print(Frequentwordsmismatch('TGCAT',5,2))
#print(Frequentwordsmismatch('AGGAGCAGCCGAAGGCAAACAAAAGGCAAACGACCAAGCCCAAGGAGGAGGCCACCAAGCAGGCCACCAAGGAGCCCACCACGAAGCCGACCAAGGCGACAAACGAAGGAGGCGAAGCAGGAGGCCACAAACGAAGCCCACGACGACGAAGGCAAAAGCCAAAAGCCGACCACAAACCACCAAGCAGGAGCCGACAAACCAAGCAGGAGCAGCCGAAGCAGGCGACGAAGCCCAAGGAGCCGACGACAAACCAAGGAGGCAAACAAACGACAAAAGGAGCCAAACGAAGCAGCAGGAGGCAAACGAAGCCCACAAAAGCCCAAGCCAAAAGCCCACAAAAGGCAAACAAACCAAGGCGAAGCCCACCACGACCACAAACCAAGGCAAACAAACGA',7,2))

def ReverseComplement(pat):
    reversecomp = []
    for i in range(len(pat)):
        if pat[i] == 'A':
            reversecomp.append('T')
        if pat[i] == 'T':
            reversecomp.append('A')
        if pat[i] == 'C':
            reversecomp.append('G')
        if pat[i] == 'G':
            reversecomp.append('C')
    reversecomp = reversecomp[::-1]
    return ' '.join([str(elem) for elem in reversecomp]).replace(' ','')

def Frequentwordsmismatchreverse(Texto, k,d):
    freqMap = {}
    patterns = []
    for i in range(len(Texto)-k+1):
        pat = Texto[i:(i+k)]
        neighborhood = list(Neighbors(pat,d))
        for j in range(len(neighborhood)-1):
            neighbor = neighborhood[j]
            if neighbor not in freqMap.keys():
                freqMap[neighbor] =1
            else:
                freqMap[neighbor] += 1
    freqMaprev ={}
    for  i in freqMap.keys():
        if i not in freqMaprev.keys() and ReverseComplement(i) not in freqMaprev.keys():
            freqMaprev[i] = freqMap[i]
        else:
            freqMaprev[ReverseComplement(i)] = freqMap[i] + freqMap[ReverseComplement(i)]

    m = Maxmap(freqMaprev)
    for i in freqMaprev.keys():
        if freqMaprev[i] == m:
            patterns.append(i)
    return patterns

#print(Frequentwordsmismatchreverse('ACGTTGCATGTCGCATGATGCATGAGAGCT',4,1))

#print(Frequentwordsmismatchreverse('TCCCCATCCTCCGTTCCCCCTCCCCCCATCCCATATTCCCCCTCCCCCCCCCTCCCCTCCCCCGTTATATATCCGTTCCCATGTTTCCTCCATGTTATCCATTCCCCCGTTTCCGTTTCCGTTGTTTCCCCGTTCCGTTATATTCCGTTATGTTGTTCCCGTTCCCATCCCCCCGTTCCCGTTCCTCCCCCATCCGTT',6,3))