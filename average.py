#average.py
#02/24/2020
#Aman Pruthi

#Part 1

#initiate as sum = 0, so that we can use it later on
sum = 0

#Define range
for i in range(1,21):
	sum = sum + i

#finding the average		
average = sum/20
print ("Part 1 - Average of first 20 natural numbers = ", average)

#Part 2
i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
import numpy as np
print("Part 2 - Average of first 20 natural numbers = ",np.mean(i))
