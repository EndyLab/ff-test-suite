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


# Detravious' code below

from random import shuffle
import random
import string_utils

def main():

# inside the ()--> (new file name, kind of access I want)
# "w"--> write and "+"-->create the file if I don't have it already
    fileForProteins = open("proteinDatabase.txt", "w+")

# write some lines of data to the file
# taking the values in the amino acid list
    aminoAcidList = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']

# {keys: values}
#     proteinsList = {'ProCoder':'A','ProTeacher':'RPE','ProTalker':'FPT'}
    proteinsSequence = ['ARF','RPANAEYVSGSICSE','FPMFARNDYECLJAFDJAFEKJSDT']
# taking the values in the amino acid list
    more1 = aminoAcidList[0] + aminoAcidList[1] + aminoAcidList[13]
    print(more1)

    bagIn = sorted(more1, key=lambda k: random.random())
    hat = ''.join(bagIn)
    for i in range(1):

        print("Is", random.sample(hat, len(hat)), " in ", proteinsSequence[0] )
        if (str(hat) in proteinsSequence[0]):
            print(True)
        else:
            print(False)
      
# writing in "proteinDatabase.txt file"
# prints a key, then its value
            fileForProteins.write(str(proteinsSequence))
# prints all of the keys first and all of the values second
            # fileForProteins.write(str(proteinsList.keys()))
            # fileForProteins.write("\n")
            # fileForProteins.write(str(proteinsList.values()))

            # fileForProteins.write(''.join(sorted(str(aminoAcidList))))
# close the file when done
    fileForProteins.close()

if __name__ == "__main__":
  main()

