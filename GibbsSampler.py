import random
import numpy as np
def CreateProfile(dnapat):
    k = len(dnapat[0])
    profile = np.zeros((4,k))

    for i in dnapat:
        for j in range(len(i)):
            if i[j] =='A':
                profile[0,j]+=1
            elif i[j] =='C':
                profile[1,j]+=1
            elif i[j] == 'G':
                profile[2,j]+=1
            elif i[j] == 'T':
                profile[3,j]+=1
    profile = profile + 1 
    profile = profile/(len(dnapat)+4)
    return profile



def GibbsSampler(Dna, k,t, N):
    dna = Dna.split()
    Motifs=[]
    for i in range(t):
        p = random.randint(0,len(dna[0])-k)
        string = dna[i]
        Motifs.append(string[p:p+k])
    BestMotifs = Motifs

    for j in range(1,N):
        i = Random(t)
        profile = 

        profile = CreateProfile(Motifs)