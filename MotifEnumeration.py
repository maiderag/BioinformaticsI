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


def MotifEnumeration(Dna,k,d):
    dna = Dna.split()
    kmerlist=[ set() for _ in dna]
    for pos, pattern in enumerate(dna):
        for k_pos in range(len(pattern)-k+1):
            kmer = pattern[k_pos:k_pos+k]
            neig = Neighbors(kmer,d)
            kmerlist[pos] = kmerlist[pos].union(neig)
    patterns = set(kmerlist[0])
    for k_set in kmerlist[1:]:
        patterns = patterns & set(k_set)
    
    return ' '.join([str(elem) for elem in patterns]).replace('','')

#print(MotifEnumeration('ATTTGGC TGCCTTA CGGTATC GAAAATT',3,1))

print(MotifEnumeration('CGGTAGTGTACCTTCCTCCATTGCC CAGCTTCAAGCGCAACGGTAACGTT CTACCGTCTTCGGTATGCTGGCACT ACGATACCGGGATTATGGTGGAAGA TGCCACGGTCTTCTGCGGACATTCA CTAAGGCTGTTCACCGGGTTATGAG',5,2))