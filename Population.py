#Poopulation estimation
#Aman Pruthi
#Feb 2, 2020

#number of years=365
#number of seconds = 365*24*60*60 = 31536000#Poopulation estimation
#Aman Pruthi
#Feb 2, 2020

#number of years=365
#number of seconds = 365*24*60*60 = 31536000

current_population = 307,357,870

years = int(input("Enter how many years: "))

birth = 31536000 / 7

death = 3153600 / 13

immigrant = 3153600 / 35

population_increase = years * (birth - death + immigrant)

print ("The population increase in", years, "years is", format(population_increase, ".2f"))
