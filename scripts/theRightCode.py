
# code working now
# next step is to find the most conserved spots


from Bio import SeqIO
from Bio import SwissProt
from Bio import pairwise2
from Bio import AlignIO
# Import format_alignment method
from Bio.pairwise2 import format_alignment
import itertools


handle = open(r"/Volumes/ENDY_LAB/code_to_test_dbs/databases/uniprot_sprot.dat")


print("\n")


# match is an int that starts at 0
# to print protein, use protein.sequence
for match, protein in enumerate(SwissProt.parse(handle)):
    for eachAA in protein, match:
# \n--> new line/ space for readability
        print("\n")
        aaSet = ['Q', 'F', 'L', 'Y', 'K', 'D', 'M', 'V', 'G', 'C', 'R', 'P', 'T', 'S', 'A']
# print statement of (-----) is used to help read the code
        print("------------------------------------------------------------")
        print("This is my set of amino acids: " + str(aaSet))
        print("------------------------------------------------------------")
# protein.sequence[0+1] starts at the first letter in a sequence and increments to the next with +1
        if protein.sequence[0+1] in aaSet:
            # print(protein.sequence[0 + 1])
            print(True)
# match is an int that starts at 0; it increments everytime and counts the total number of proteins
            print("Protein sequence in database: ", match+1)
            db = list(protein.sequence)
# .join turns list into strings
            db = ''.join(db);
            print(db)
            print("------------------------------------------------------------")
            break
        else:
            print("\n")
# to test logic/ if failed, then uncomment the lines below
            # print(False)
            # print("Protein sequence in database: ", match+1)
            # db = list(protein.sequence)
            # db = ''.join(db);
            # print(db)
            # print("------------------------------------------------------------")
