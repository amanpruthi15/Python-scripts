# Littlelists.oy
# Aman Pruthi
# 12 April 2020

print("#######################")
string = "The quick brown fox jumped over the lazy dog"
print("Finding the number of spaces in the string")
print ("String is - ",string,"\n")
print("Firstly, doing it with the help of loop")
space=[]
for s in string:
	if s.count(" ")>0:
		space.append(s)		
print("The number of spaces in the string are: ",len(space))
print("#######################")

print("Secondly, with the help of list comprehension")
spaces=[s for s in string if s.count(" ")>0]
print("The number of spaces in the string are: ",len(spaces))
print("#######################\n")

words = string.split(" ")
print("Finding the words with the letter o with the help of loop")
number_o = []
for x in words:
	if x.count("o")>0:
		number_o.append(x)
print ("The words with the letter o in the string are: ",number_o)
print("#######################")

print("The same thing with the help of list comprehension")
number_o_ = [x for x in words if x.count("o")>0]
print ("The words with the letter o in the string are: ", number_o_) 
print("#######################\n")

print("Finding all the words that have atleast 5 letters in above string")
print("First with the help of loop:")
number_O =[]
for y in words:
	if len(y)>=5:
		number_O.append(y)
print("The words with alteast 5 letters are :",number_O)
print("#######################")

print("Secondly, with the help of list comprehension")
number_O_=[y for y in words if len(y)>=5]
print("The words with the atleast 5 letters are: ",number_O_)
print("#######################\n")

print("Finding all the number that contain 3 from 1-1000")
print("Firstly, doing it by the loop:")
number_3=[]
for z in list(range(1,1000)):
	if str(z).count("3")>0:
		number_3.append(z)
print("The numbers that have 3 in them are:\n ",number_3)
print("#######################")

print("Secondly, doing the same thing with list comprehension")
number_3_=[z for z in list(range(1,1000)) if str(z).count("3")>0]
print("The numbers that have 3 in them are:\n", number_3_)
