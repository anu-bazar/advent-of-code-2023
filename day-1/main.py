#print("Hello World")
import re
# Using readlines()
file1 = open('day-1\input.txt', 'r')
Lines = file1.readlines()
#print(Lines)
#create empty list
elf_numbers=[]
for line in Lines:
    numbers = re.findall(r'\d+', line)
    elf_numbers.append(numbers)
#print(len(elf_numbers))

final_numbers = []
for number1 in elf_numbers:
    first_number = (number1[0])[0]
    last_number = (number1[-1])[-1]
    variable=first_number+last_number
    final_numbers.append(variable)
#print((final_numbers))

final_sum=[int(x) for x in final_numbers]
print(sum(final_sum))
	
#close your reader
file1.close()
#answer 55971