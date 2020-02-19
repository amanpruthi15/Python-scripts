#countingbases.py
#Aman Pruthi
#February 17, 2020

import random
bases = ["A","C","T","G"]
sequence = random.choices(bases,k=100)
print(sequence)

G_string = sequence.count('G')
A_string = sequence.count('A')
A_and_C_string = sequence.count('A') + sequence.count('C')

string1 = "Number of G's = "
string2 = "Number of A's = "
string3 = "Number of A's + C's = "

print (string1 + str(G_string))
print (string2 + str(A_string))
print (string3 + str(A_and_C_string))

