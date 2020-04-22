# GC content
# 21 April, 2020
# Aman Pruthi

# Calculating the GC content 

#########################
# 1. Generating a random RNA sequence of 5000 bp
########################
import random
bases = ['A', 'U', 'G', 'C']
RNA = random.choices(bases, k=5000)
mRNA = ''.join(RNA)
print('\nRandomly generated mRNA seqeunce is:\n\n',mRNA)

########################
# Breaking the mRNA into 100 small pieces
#######################
split = []
n = 100
for index in range(0, len(mRNA), n):
	split.append(mRNA[index : index + n])
print('\nThe smaller sequences formed after breaking the bigger sequence at 100 nt:\n\n',split)

#######################
# Calculating the GC content
#######################
def GC(split):
	GC_count = ((split.count("G") + split.count("C"))/100)*100
	return (GC_count)

GC_split = [GC(index) for index in split]
print('\nThe percentage of GC content in all the smaller sequences:\n\n',GC_split)
