'''
Find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.

Need to find all of the instances of XMAS. 

'''

from typing import Counter

# sample_input = [
#     list("MMMSXXMASM"),
#     list("MSAMXMSMSA"),
#     list("AMXSXMAAMM"),
#     list("MSAMASMSMX"),
#     list("XMASAMXAMM"),
#     list("XXAMMXXAMA"),
#     list("SMSMSASXSS"),
#     list("SAXAMASAAA"),
#     list("MAMMMXMMMM"),
#     list("MXMXAXMASX")
# ]

# Reading in Input
input = open("Day4/Day4Inp.txt").read().strip()
#print(input)
# Convert the input into a 2D list (grid)
grid = [list(line) for line in input.splitlines()]
#print(grid)


def find_xmas(grid):
  directions = [
      (0, 1),  # right, horizontal
      (0, -1),  # left, horizontal
      (1, 0),  # up, vertical
      (-1, 0),  # down, vertical
      (1, 1),  # up right, diagonal
      (-1, -1),  # down left, diagonal
      (1, -1),  # up left, diagonal
      (-1, 1)  # down right, diagonal
  ]
  word = "XMAS"
  rows, cols = len(grid), len(grid[0])
  results = []

  for r in range(rows):
    for c in range(cols):
      for dr, dc in directions:
        match = True
        for i in range(len(word)):
          nr, nc = r + dr * i, c + dc * i
          if not (0 <= nr < rows
                  and 0 <= nc < cols) or grid[nr][nc] != word[i]:
            match = False
            break
        if match:
          results.append((r, c, dr, dc))  # Store start and direction
  return results


print(len(find_xmas(grid)))
'''
Notes to Self

At each index in the grid, look horizontally, vertically, diagonally, and backwards for the word XMAS. If not applicable, replace the current index with a '.' and move to next index

At the element you're currently looking at, look in each of the 8 possible directions (if applicable)). If the word is found, return True. If not, return False. For example for an x in the [0][0] element of the grid, I can only look rightwards, downwards, and right diagonally.

'''
