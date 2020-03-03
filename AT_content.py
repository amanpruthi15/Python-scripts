# AT content
# Aman Pruthi
# March 1, 2020
# Calculate the AT content in a short DNA sequence

#####################
# Basic Steps
#####################
# 1. Print the list of nucleotides
# 2. Calculate the number of A and T
# 3. Caluclate the total number of nucleotides 
# 4. Calculating percentage AT content

sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print ("The sequence is: ", sequence)
print ("######################")

#####################
# Calculating the number of A and T
A_count = sequence.count("A")
T_count = sequence.count("T")
AT = A_count + T_count
print ("Total number of A and T = ", str(AT))
print ("######################")

# Caulcating the total number of nucleotides
Total = len(sequence)
print ("The total number of nucleotides = ", Total)
print ("######################")

# Calculating percentage AT content
Percent_AT = AT/Total * 100
print ("Percentage of AT content = ", Percent_AT)
