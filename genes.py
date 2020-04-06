# Aman Pruthi
# genes.py
# 4 April, 2020
# Finding the length of the genes

#########################
# Basic Steps
#########################
# 1. Generating a random RNA sequence of 1000 bp
# 2. Create a list genes starting from AUG
# 3. Create a list of large genes
# 4. Determine the length of large genes

#########################
# Starting the command line
#########################

#########################
# 1. Generating a random RNA sequence of 1000 bp
########################
import random
bases = ['A', 'U', 'G', 'C']
RNA = random.choices(bases, k=1000)
mRNA = ''.join(RNA)
print('\nRandomly generated mRNA seqeunce is:\n\n',mRNA)

#########################
# 2. Create a list genes starting from AUG
#########################
split = mRNA.split('AUG')
print("\nIf we split the sequence at every start codon i.e. AUG the genes that will be formed are:\n\n",split)
length = len(split)
print ('\nThe number of genes formed are:',length)

########################
# 3. Create a list of large genes
########################
largegenes=[]
 
for i in split:
	if len(i) > 50:
		largegenes.append(i)
print("\nThe list of large genes is as follows:\n\n", largegenes)

########################
# 4. Determine the length of large genes
########################
print ("\nThe length of the large genes are:\n")
for a in largegenes:
	print(len(a))
