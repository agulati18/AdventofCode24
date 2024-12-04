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
#print(numbers)

# Aggregate Sum Counter
aggregate_sum = 0

# Iterate over the numbers, multiply the pairs, and calculate the sum
for x, y in numbers:
    product = x * y
    aggregate_sum += product

# Print the Result
print(f'Aggregate Sum: {aggregate_sum}')

### Puzzle 2
'''
1. The do() instruction enables future mul instructions. do() is on. Everything after it, till a dont() is reached is valid for being included in final sum.

2. The don't() instruction disables future mul instructions. don't() is off. Everything after it, till a do() is reached is invalid for being included in final sum.

Only the most recent do() or don't() instruction applies.
At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. 

The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

'''

# Cut down this overall input into a subspace, with only do() and dont() and mul(x,y) instructions

# Define the regex pattern for matches to keep
pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"

# Find all matches in the input string
matches = re.findall(pattern, input)

# In this for loop, I want to iterate over the matches. If the mul(x,y) is after a do() or not after a dont() instruction, then I want to add it to the aggregate sum. If the mul(x,y) is after a don't() instruction, then I don't want to add it to the aggregate sum.
aggregated_sum = 0
# Track state if mul instructions are enabled
enabled = True

for match in matches:
  if match == "do()":
      enabled = True
  elif match == "don't()":
      enabled = False
  # Using a while loop here leads to an infinite loop on the first element because the 1st element is enabled by default. Use if.
  if enabled:
    numbers = re.findall(r'\d+', match)
    #print(numbers)
    if len(numbers) != 0:
      x, y = map(int, numbers)
      #print(x, y)
      product = x * y
      aggregated_sum += product

# Print the aggregate sum
print(f'Aggregated Sum (with enabler): {aggregated_sum}')
