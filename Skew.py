def Skew(Genome):
    skew = [0]
    for i in Genome:
        if i == 'G':
            skew.append(skew[-1]+1)
        elif i == 'C':
            skew.append(skew[-1]-1)
        else:
            skew.append(skew[-1])
    
    return skew

def get_minvalue(inputlist):
 
    #get the minimum value in the list
    min_value = min(inputlist)
 
    #return the index of minimum value 
    res = [i for i,val in enumerate(inputlist) if val==min_value]
    return res

print(Skew('CATGGGCATCGGCCATACGCC'))

print(Skew('GAGCCACCGCGATA'))

a =Skew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')
#print(get_minvalue(a))
import os
print(os.getcwd())
f = open("courserabioinfo/Week 2/dataset_7_10.txt", "r")
genome = f.readline()
b=Skew(genome)
print(get_minvalue(b))


a = Skew('CATTCCAGTACTTCATGATGGCGTGAAGA')
print(a)
print(max(a))
print(a.index(max(a)))