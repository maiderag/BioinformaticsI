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

#print(ReverseComplement('AAAACCCGGT'))

print(ReverseComplement('TTGTGTC'))