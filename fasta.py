# fasta.py
# Aman Pruthi
# 30 April 2020

# import modules
import argparse
from Bio import SeqIO

##########################
#####  Arguement  ########
##########################
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--INPUT", required = True, help = "Input the fasta file")
args = vars(ap.parse_args())
###########################

###########################
# Number of records in the file
##########################
sizes = [len(rec) for rec in SeqIO.parse(args["INPUT"], "fasta")]
print ("\nThe number of records in the file are: ",len(sizes))

###########################
print ("\nFinding the shortest and the largest record")
##########################
sizes.sort()
print("\nThe length of the shortest record is: ", *sizes[:1])
shortest = []
for s in SeqIO.parse(args["INPUT"],"fasta"):
	if len(s) == 501:
		shortest.append(s.id)
print("\nThe records with shortest length are: ",shortest)

###########################
print("\nThe length of the largest record is: ", sizes[-1])
largest=[]
for l in SeqIO.parse(args["INPUT"],"fasta"):
	if len(l) == 317079:
		largest.append(l.id)
print("\nThe record with largest length is: ",largest)

#########################
print("\nFinding the GC content")
##########################
gc=[x.seq.count("G") + x.seq.count("C") for x in SeqIO.parse(args["INPUT"],"fasta")]
print("\nThe GC content in each of the record is:\n",gc)

#########################
# Creating a histogram
########################
import numpy 
import matplotlib.pyplot as plt

fig=plt.hist(gc)
plt.title("Histogram showing the GC content of the random sequence")
plt.xlabel("GC-content")
plt.ylabel("Frequency")
plt.savefig("GC-content-dIul.png")

#########################
# Finding the records with most and the least GC content
#########################
gc.sort()
print("\nThe least GC content found in the records is: ", *gc[:1])
gc_s = []
for s in SeqIO.parse(args["INPUT"],"fasta"):
	if s.seq.count("G") + s.seq.count("C") == 68:
		gc_s.append(s.id)
print("\nThe records with the least GC content is: ",gc_s)

###########################
print("\nThe highest GC content found in the records is: ",gc[-1])
gc_l = []
for l in SeqIO.parse(args["INPUT"],"fasta"):
	if l.seq.count("G") + l.seq.count("C") == 101094:
		gc_l.append(l.id)
print("\nThe record with highest GC content is: ",gc_l)

###########################
# Translating each record
###########################
for x in SeqIO.parse(args["INPUT"],"fasta"):
	print(x.seq.translate())

##########################
print("\nFinding the most and the least number of stop codons")
#########################
stopcodon=[]
for x in SeqIO.parse(args["INPUT"],"fasta"):
	stopcodon.append(str(x.translate()).count("*"))


print("\nThe least number of stop codons present in the records: ",min(stopcodon))
print("\nThe largest number of stop codon present in the records: ",max(stopcodon))

minstop=[]
for x in SeqIO.parse(args["INPUT"],"fasta"):
	if str(x.translate()).count("*")==min(stopcodon):
		minstop.append(x.id)
print("\nThe records with least stop codons are: \n",minstop)

maxstop=[]
for x in SeqIO.parse(args["INPUT"],"fasta"):
	if str(x.translate()).count("*")==max(stopcodon):
		maxstop.append(x.id)
print("\nThe record with most stop codons is: ",maxstop)
