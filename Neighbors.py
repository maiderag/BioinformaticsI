# def InmediateNeighbors(pat):
#     Neighborhood = [pat]
#     nucleotide = {'A','C','G','T'}
#     for i in range(1, len(pat)):
#         symbol = pat[i]
#         for j in nucleotide:
#             if j!=symbol:
#                 Neighbor=pat[:i]+j+pat[i+1:]
#                 Neighborhood.append(Neighbor)
#     return Neighborhood

# print(InmediateNeighbors('AATAC'))

# def Neighbors(pat):
#     Neighborhood = [pat]
#     nucleotide = {'A','C','G','T'}
#     pat1=pat[1:]
#     Neigh =[]
#     for i in range(len(pat1)):
#         symbol = pat1[i]
#         for j in nucleotide:
#             if j!=symbol:
#                 Neighbor=pat1[:i]+j+pat1[i+1:]
#                 Neighborhood.append(Neighbor)
#                 Neigh.append(pat[0]+Neighbor)
#     for i in range()
#     Neigh.append(pat[0]+Neighborhood[-1])
#     Neigh.append(nucleotide+pat[-1])
#     return Neigh

# print(Neighbors('CAA'))

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

print(Neighbors('ACG',1)) 

print(' '.join([str(elem) for elem in list(Neighbors('CTTATTAT',2))]).replace(' ',' '))