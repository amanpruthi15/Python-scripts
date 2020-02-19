#bats.py
#Aman Pruthi
#February 17,2020

#Name of the species
first = input("What is the name of the first species?")
second = input("What is the name of the second species?")
third = input("What is the name of the third species?")

#Capitalization and abbreviation
sp1 = (first.split(' ')[0][:3] + first.split(' ')[1][:3]).upper()
sp2 = (second.split(' ')[0][:3] + second.split(' ')[1][:3]).upper()
sp3 = (third.split(' ')[0][:3] + third.split(' ')[1][:3]).upper()

print (sp1 + '\n' + sp2 + '\n' + sp3)
