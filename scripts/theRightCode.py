
# code working now
# next step is to find the most conserved spots
# figure out the meaning of each attribute; search through actual database

from Bio import SeqIO
from Bio import SwissProt
from Bio import pairwise2
from Bio import AlignIO
# Import format_alignment method
from Bio.pairwise2 import format_alignment
import itertools

# handle = open(r"/Volumes/ENDY_LAB/code_to_test_dbs/databases/test.dat")

handle = open(
    r"/Volumes/ENDY_LAB/code_to_test_dbs/databases/uniprot_sprot.dat")


# match is an int that starts at 0
# to print protein, use protein.sequence
for match, protein in enumerate(SwissProt.parse(handle)):
    g = True
    # print("Testing protein ", match+1)

    # for eachAA in protein, match:

# \n--> new line/ space for readability
    # print("\n")
    aaSet = ['Q', 'F', 'L', 'Y', 'K', 'D', 'M',
             'V', 'G', 'C', 'R', 'P', 'T', 'S', 'A']
    aaSetPrintable = ''.join(aaSet)
    # aaSetTwo = ['N','E', 'H', 'I', 'W', 'Q', 'F', 'L', 'Y', 'K', 'D', 'M', 'V', 'G', 'C', 'R', 'P', 'T', 'S', 'A']
# print statement of (-----) is used to help read the code

# protein.sequence[0+1] starts at the first letter in a sequence and increments to the next with +1
    for n in range(0, len(protein.sequence)):
            # letter +=1
            # print (len(protein.sequence))
            # print(n)
            # print("Print letter: ", match)
        if protein.sequence[n] not in aaSet:
            g = False
            # print(protein.sequence[n])
            # print(len(protein.sequence))
            # print(protein.sequence[0 + 1])
            # print(True)
            break
    if g == True and (len(protein.sequence)) >= 50:

        print("\n")
        print("Reduced amino acid set = [" + aaSetPrintable + "]")
        print("\n")

# match is an int that starts at 0; it increments everytime and counts the total number of proteins
        print("Matching Protein")
        print("Index = " + str(match+1))
        db = list(protein.sequence)
# .join turns list into strings
        print("Description = " + str(protein.description))
        print("Features = " + str(protein.features[0]))
        db = ''.join(db)
        print("Sequence = " + str(db))
        print("Length = " + str(len(protein.sequence)))
        print("\n")
        print("------------------------------------------------------------")
        # break
        # else:
        # print("\n")
# to test logic/ if failed, then uncomment the lines below
        # print(False)
        # print("Protein sequence in database: ", match+1)
        # db = list(protein.sequence)
        # db = ''.join(db);
        # print(db)
        # print("------------------------------------------------------------")
