def Text(i, k, Pat):
    return (Pat[i:(i+k)])

def PatternMatching(Pat, Genome):
    startingpos = []
    for i in range(len(Genome)-len(Pat)+1):
        if Text(i, len(Pat), Genome) == Pat:
            startingpos.append(i)
    return ' '.join([str(elem) for elem in startingpos])

#print(PatternMatching('ATAT','GATATATGCATATACTT'))


#import os

#f = open("vibrio.txt", "r")
#f1 = open("salida.txt", "w")
#genome = f.readline()
#print(PatternMatching('CTTGATCAT',genome))
#f1.write(PatternMatching('CTTGATCAT', genome))
#f1.close()
#f.close()

print(PatternMatching('CGC', 'ATGACTTCGCTGTTACGCGC'))
