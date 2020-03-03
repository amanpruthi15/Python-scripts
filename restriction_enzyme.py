# Restriction digestion
# Aman Pruthi
# March 1, 2020
# Count the length of the fragments produced by restriction digestion

#########################
# Basic Steps
#########################
# 1. Define the sequence
# 2. Define the site of digestion
# 3. Split the sequence at the site of digestion
# 4. Count the number of bases in each fragment
#########################

########################
# Detailed Steps
#######################
# 1. Define the sequence
#   - Make a string of the sequence
# 2. Define the site of digestion
#   - Make a string of the digestion site
# 3. Split the sequence at the site of digestion
#   - Divide the GAATTC at the site of the cut to make two fragments
# 4. Count the number of bases in each fragment
#   - Count the number of bases for fragment 1
#   - Count the number of bases for fragment 2

#######################
# Starting the command line
#######################

# Defining the sequence
sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print ("The sequence needed to be digested by restriction enzyme: ", sequence)
print ("########################")
#####################
# Defining the restriction site
site = "GAATTC"
restriction = sequence.find(site)
print ("Restriction site of E.coli: G-AATTC")
print ("########################")
#####################

digestion = restriction + 1

######################
# Defining the two fragments

first_fragment = sequence[:digestion]
second_fragment = sequence[digestion:]
print ("The first fragment produced is: ", first_fragment)
print ("The second fragment produced is: ", second_fragment)
print ("########################")

######################
# Counting the length of each fragment

first = len(first_fragment)
second = len(second_fragment)
print ("The size of first fragment is: ", first)
print ("The size of the second fragment is: ", second)
