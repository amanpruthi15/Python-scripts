# Argparse GC content
# Aman Pruthi
# 20 April, 2020

# import modules
import random
import argparse

#########################
###### Arguments ########
#########################

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--SIZE", required = True, type = int, help = "Enter the size of the sequence")
ap.add_argument("-m", "--SMALLER_SEQUENCES", required = True, type = int, help = "Enter the size of the smaller sequences")
args=vars(ap.parse_args())

#########################
# Generating a random RNA sequence
#########################
bases = ['A', 'U', 'G', 'C']
RNA = random.choices(bases, k = (args["SIZE"]))
mRNA = ''.join(RNA)
print('\nRandomly generated mRNA seqeunce is:\n\n',mRNA)

########################
# Breaking the mRNA into small pieces
#######################
split = []
for index in range(0, args['SIZE'], args['SMALLER_SEQUENCES']):
        split.append(mRNA[index : index + args['SMALLER_SEQUENCES']])
print('\nThe smaller sequences formed after breaking the bigger sequence:\n\n', split)

#######################
# Calculating the GC content
#######################
def GC(split):
        GC_count = ((split.count("G") + split.count("C"))/100)*100
        return (GC_count)

GC_split = [GC(index) for index in split]
print('\nThe percentage of GC content in all the smaller sequences:\n\n',GC_split)

##########################
### Plotting histogram ###
##########################

import numpy 
import matplotlib.pyplot as plt

fig=plt.hist(GC_split)
plt.title("Histogram showing the GC content of the random sequence")
plt.xlabel("GC-content")
plt.ylabel("Frequency")
plt.savefig("GC-content.png")
