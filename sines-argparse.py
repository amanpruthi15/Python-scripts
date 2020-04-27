# Using Argparse
# Aman Pruthi
# 26 April, 2020
# Using various commands in Pandas

# import modules
import pandas as pd
import argparse

############################
# Basic Steps
# 1. Assign column names
# 2. Determining the families
# 3. Creating a new dataframe
# 4. Drop some columns
# 5. Create a new column
# 6. Determine the min, max and mean for all SINEs
# 7. Determine the min, max and mean for sub-families of SINE (metulj and ZenoSINE)

##########################
#####  Arguement  ########
##########################
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--INPUT", required = True, help = "Input the bed file")
ap.add_argument("-f", "--FAMILY", required = True, help = "Select one family")
ap.add_argument("-g", "--GENOME_SIZE", required = True , type = int, help = "Select the genome size")
argv = vars(ap.parse_args())
###########################

# Starting the command line
# 1. Assign column names

print("####################")
# Rename columns
print ("Renaming columns....")
fields = ["Scaffold", "Start", "Stop", "Element", "Score", "Strand", "Family", "Sub-Family", "Divergence"]
bed = pd.read_csv ("aVan_rm.bed", names = fields, sep ="\t")
print(bed.head())

##########################
print("####################")
# 2. Determining the families
family = bed.Family.unique()
print ("The unique families in the bed file are: ", family)

##########################
print("####################")
# 3. Creating a new dataframe
new_data = bed[bed['Family'] == argv['FAMILY']]
print ("The new dataframe formed from the SINE elements in family is: ", '\n', new_data.head())

#########################
print("####################")
# 4. Drop some columns
new_data = new_data.drop(["Strand", "Score"], axis = 1)
print ('After dropping 2 columns the data looks like: ,' '\n', new_data.head())

#########################
print("####################")
# 5. Create a new column
new_data["Length"] = new_data['Stop'] - new_data['Start']
print ('Insertion of the length column in the data: ', '\n', new_data.head())

#########################
print("####################")
# 6. Determine the min, max and mean of SINEs
min = new_data["Length"].min()
print ("The minimum value for all SINEs is: ",min)

max = new_data["Length"].max()
print ("The maximum value for all SINEs is: ",max)

mean = new_data["Length"].mean()
print ("The mean value for all SINEs is: ",mean)

#########################
print("####################")
# 7. Determine the min, max and mean for sub-families of SINE (metulj and ZenoSINE)
subfam_min = new_data.groupby("Sub-Family")["Length"].min()
print ("Minimum value of the sub families are: ", "\n", subfam_min)

subfam_max = new_data.groupby("Sub-Family")["Length"].max()
print ("Maximum value of the sub families are: ", "\n", subfam_max)

subfam_mean = new_data.groupby("Sub-Family")["Length"].mean()
print ("Mean value of the sub families are: ", "\n", subfam_mean)

# Create a new column called proportion
new_data['Proportion'] = new_data['Length']/argv["GENOME_SIZE"]

# Create a new dataframe
new_data.to_csv("aVan.csv")
