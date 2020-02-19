#bats.py
#Aman Pruthi
#February 17, 2020

first = input("What is the name of the first species?")
second = input("What is the name of the second species?")
third = input("What is the name of the third species?")

capitalize_first = first.upper()
capitalize_second = second.upper()
capitalize_third = third.upper()

string = "There are three species of bats:"
print(string)
print(capitalize_first[:3] + capitalize_first[7:10])
print(capitalize_second[:3] + capitalize_second[7:10])
print(capitalize_third[:3] + capitalize_third[10:13])
