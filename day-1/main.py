#print("Hello World")
import re
# Using readlines()
file1 = open('day-1\input.txt', 'r')
Lines = file1.readlines()
#print(Lines)
#create empty list
elf_numbers=[]
for line in Lines:
    numbers = re.findall(r'\d+', line) #'/d' - digit from 0 to 9 AND '+' - one or more occurences 
    for number in numbers:
        elf_numbers.append(int(number))
#print(elf_numbers)






"""if its a letter, then do not extract
if its a number then do extract and store it into a new line
	if the number is higher than 2
	take the 1st number and last number
	if the number is 2
	take the 1st number and last number
	if the number is one
	the number should be doubled """


		

#close your reader
file1.close()
