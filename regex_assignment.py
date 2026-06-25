import re

# File ko open karna (Apni download ki hui actual file ka sahi naam check kar lijiye)
file_name = "regex_sum_2418144.txt"
try:
    handle = open(file_name)
except:
    print("File open karne mein dikkat aa rahi hai. Path check karein.")
    quit()

total_sum = 0
count = 0

# Line-by-line streaming loop
for line in handle:
    line = line.rstrip()
    
    # Isolate all numbers in the current line using regex set modifier [0-9]+
    numbers = re.findall('[0-9]+', line)
    
    # Agar line mein koi number nahi mila, toh skip karein
    if len(numbers) < 1: 
        continue
        
    # Loops elements matrix to parse string variables into actual integers
    for num in numbers:
        total_sum = total_sum + int(num)
        count = count + 1

# Results extraction metrics console logs
print("Total integers found:", count)
print("The calculated absolute total sum is:", total_sum)