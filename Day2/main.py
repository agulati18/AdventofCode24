'''
The engineers are trying to figure out which reports are safe

A report only counts as safe if both of the following are true:
  i) The levels are either all increasing or all decreasing.
  ii) Any two adjacent levels differ by at least one and at most three.

Examples: 
7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
'''

# Reading in the data from input.txt
# Step 1: Split the text into lines
lines = open("Day2/input2.txt").read().strip().splitlines()
# Step 2: Process each line
data = [list(map(int, line.split())) for line in lines]
# Output the processed data
print(data)
is_safe = 0


def is_safe_report(levels):
  # Check Monotoicity
  # Check if all items in the list are Increasing:
  increasing = all(levels[i] <= levels[i + 1] for i in range(len(levels) - 1))
  # Check if all items in the list are Decreasing:
  decreasing = all(levels[i] >= levels[i + 1] for i in range(len(levels) - 1))
  if not (increasing or decreasing):
    return False

  # Check Adjacent Difference
  for i in range(len(levels) - 1):
    # Check if the difference between the current and next item is greater than 3
    if abs(levels[i] - levels[i + 1]) > 3:
      return False
    # Check if the difference between the current and next item is greater than 3
    if abs(levels[i] - levels[i + 1]) < 1:
      return False

  return True


# Output the processed data
for line in data:
  if is_safe_report(line):
    is_safe += 1
print(is_safe)
