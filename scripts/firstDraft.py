## iterating through the full set of 20 amino acids and printing all possible\
## subsets of size 1 to n = 20 as strings

import itertools;

fullAminoAcids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N',\
'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'];

# red15AminoAcids = ['A', 'D', 'F', 'G', 'K', 'L', 'M', 'P', 'Q', 'R', 'S', 'T',\
# 'V', 'W', 'Y'];

for n in range(1, 3):   # endrange = (len(fullAminoAcids)+1)

    for aaSubset in itertools.combinations(fullAminoAcids, n):  # creates subsets as tuples

        aaSubset = ''.join(aaSubset);   # convert aaSubset to type string
        print (aaSubset);

## test Python capability to iterate through individual elements of a string

# testString = 'ABCD';
# for each in testString:
#     print (each);
