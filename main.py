# Initialize empty lists
left_column = []
right_column = []

# Read and process the data from input.txt
with open('input.txt', 'r') as file:
  for line in file:
    # Skip empty lines
    if line.strip():
      left, right = line.split()
      left_column.append(int(left))
      right_column.append(int(right))

# Print the results
# print("Left Column:", left_column)
# print("Right Column:", right_column)

diff = 0

# Sort Lists - .sort() sorts in place whereas sorted() returns a new list
left_sort = sorted(left_column)
right_sort = sorted(right_column)

# Difference Calculation

for i in range(len(left_sort)):
  diff += abs(left_sort[i] - right_sort[i])

print("Difference:", diff)

# Similarity Calculation
### Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
###The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
### The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
### The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).

similarity = 0
for i in range(len(left_sort)):
  # get the base number from left_sort and then multiply that by the number of times it appears in the right_sort
  # The count() method returns the number of elements with the specified value.
  similarity += left_sort[i] * right_sort.count(left_sort[i])
print("Similarity:", similarity)
