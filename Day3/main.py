import re

input = open("Day3/day3inp.txt").read().strip()
#print(input)

# Pattern: mul(x,y)
pattern = r"mul\(\d+,\d+\)"

# Find all matches for the pattern
matches = re.findall(pattern, input)
#print(matches)

# Extract only the numbers from the matches (re.findall(r'\d+,\d+', ",")) and convert them to integers
numbers = [(int(x), int(y)) for x, y in (match.split(',') for match in re.findall(r'\d+,\d+', ",".join(matches)))]
print(numbers)

# Aggregate Sum Counter 
aggregate_sum = 0

# Iterate over the numbers, multiply the pairs, and calculate the sum
for x, y in numbers:
    product = x * y
    aggregate_sum += product

# Print the Result
print(aggregate_sum)
  

  
# aggregated_result += (x * y)
# print(aggregated_result)